#!/usr/bin/env python3
"""KISWARM6.0 - Master KISWARM API Server"""
from flask import Flask, jsonify, request
from flask_cors import CORS
import json, time, uuid, os

app = Flask(__name__)
CORS(app)

STATE_FILE = "/tmp/kiswarm_state.json"
MESSAGES_FILE = "/tmp/kiswarm_messages.json"
CHAT_FILE = "/tmp/kiswarm_chat.json"
SHADOW_FILE = "/tmp/kiswarm_shadow.json"
TUNNEL_FILE = "/tmp/kiswarm_tunnels.json"

def load_json(path, default):
    try:
        if os.path.exists(path):
            with open(path, 'r') as f:
                return json.load(f)
    except: pass
    return default

def save_json(path, data):
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)

# Initialize
for f, d in [(STATE_FILE, {"mesh_status": "online", "nodes": {}, "statistics": {"messages_total": 0}}),
             (MESSAGES_FILE, {"pending": [], "processed": []}),
             (CHAT_FILE, {"messages": []}),
             (SHADOW_FILE, {"nodes": {}}),
             (TUNNEL_FILE, {"tunnels": {}})]:
    if not os.path.exists(f):
        save_json(f, d)

# --- LAYER 1: SCADA CONTROL (Status & Register) ---
@app.route('/api/mesh/status', methods=['GET'])
def get_status():
    state = load_json(STATE_FILE, {})
    return jsonify({"status": "online", "mesh_status": state.get("mesh_status", "unknown"),
                    "nodes_count": len(state.get("nodes", {})), "timestamp": time.time()})

@app.route('/api/mesh/state', methods=['GET'])
def get_state():
    return jsonify(load_json(STATE_FILE, {}))

@app.route('/api/mesh/messages', methods=['GET'])
def get_messages():
    data = load_json(MESSAGES_FILE, {"pending": []})
    messages = data["pending"][:50]
    return jsonify({"count": len(messages), "messages": messages, "timestamp": time.time()})

@app.route('/api/mesh/register', methods=['POST'])
def register():
    data = request.json or {}
    installer_id = str(uuid.uuid4())
    state = load_json(STATE_FILE, {"nodes": {}})
    state["nodes"][installer_id] = {
        "node_id": installer_id,
        "node_name": data.get("installer_name", "unknown"),
        "environment": data.get("environment", "unknown"),
        "capabilities": data.get("capabilities", []),
        "status": "online",
        "last_seen": time.time()
    }
    state["statistics"] = {"messages_total": state.get("statistics", {}).get("messages_total", 0) + 1}
    save_json(STATE_FILE, state)
    print(f"[REGISTER] {data.get('installer_name')} -> {installer_id}")
    return jsonify({"installer_id": installer_id, "status": "registered",
                    "message": "Welcome to Master KISWARM!"})

@app.route('/api/mesh/status/<installer_id>', methods=['POST'])
def report_status(installer_id):
    data = request.json or {}
    msgs = load_json(MESSAGES_FILE, {"pending": []})
    msgs["pending"].append({
        "message_id": str(uuid.uuid4()),
        "message_type": "status_update",
        "sender_id": installer_id,
        "timestamp": time.time(),
        "payload": data
    })
    save_json(MESSAGES_FILE, msgs)
    state = load_json(STATE_FILE, {"nodes": {}})
    if installer_id in state.get("nodes", {}):
        state["nodes"][installer_id]["status"] = data.get("status")
        state["nodes"][installer_id]["last_seen"] = time.time()
        save_json(STATE_FILE, state)
    print(f"[STATUS] {installer_id[:8]}...: {data.get('status')} - {data.get('task', '')} ({data.get('progress', 0)}%)")
    return jsonify({"status": "acknowledged"})

@app.route('/api/mesh/error/<installer_id>', methods=['POST'])
def report_error(installer_id):
    data = request.json or {}
    msgs = load_json(MESSAGES_FILE, {"pending": []})
    msgs["pending"].append({
        "message_id": str(uuid.uuid4()),
        "message_type": "error_report",
        "sender_id": installer_id,
        "priority": 0,
        "timestamp": time.time(),
        "payload": data
    })
    save_json(MESSAGES_FILE, msgs)
    print(f"[ERROR] {installer_id[:8]}...: {data.get('error_type')} - {data.get('error_message')}")
    return jsonify({"status": "acknowledged", "message": "Error logged, awaiting fix from Z.ai"})

@app.route('/api/mesh/fix', methods=['POST'])
def send_fix():
    data = request.json or {}
    installer_id = data.get("installer_id")
    msgs = load_json(MESSAGES_FILE, {"pending": []})
    msgs["pending"].append({
        "message_id": str(uuid.uuid4()),
        "message_type": "fix_suggestion",
        "sender_id": "z_ai",
        "receiver_id": installer_id,
        "timestamp": time.time(),
        "payload": data
    })
    save_json(MESSAGES_FILE, msgs)
    print(f"[FIX] Sent to {installer_id[:8] if installer_id else 'unknown'}...: {data.get('title', '')}")
    return jsonify({"status": "queued", "fix": data, "timestamp": time.time()})

@app.route('/api/mesh/abort', methods=['POST'])
def abort():
    data = request.json or {}
    installer_id = data.get("installer_id")
    msgs = load_json(MESSAGES_FILE, {"pending": []})
    msgs["pending"].append({
        "message_id": str(uuid.uuid4()),
        "message_type": "abort",
        "sender_id": "z_ai",
        "receiver_id": installer_id,
        "timestamp": time.time(),
        "payload": {"reason": data.get("reason", "Aborted")}
    })
    save_json(MESSAGES_FILE, msgs)
    print(f"[ABORT] Sent to {installer_id[:8] if installer_id else 'unknown'}...")
    return jsonify({"status": "queued"})

@app.route('/api/mesh/heartbeat/<installer_id>', methods=['POST'])
def heartbeat(installer_id):
    state = load_json(STATE_FILE, {"nodes": {}})
    if installer_id in state.get("nodes", {}):
        state["nodes"][installer_id]["last_seen"] = time.time()
        save_json(STATE_FILE, state)
    return jsonify({"status": "acknowledged"})


# --- LAYER 2: A2A CHAT (Direct Agent Communication) ---
@app.route('/api/mesh/chat/send', methods=['POST'])
def send_chat():
    data = request.json or {}
    chat = load_json(CHAT_FILE, {"messages": []})
    message = {
        "id": str(uuid.uuid4()),
        "from": data.get("from", "unknown"),
        "to": data.get("to", "all"),
        "message": data.get("message", ""),
        "timestamp": time.time()
    }
    chat["messages"].append(message)
    # Keep last 100 messages
    chat["messages"] = chat["messages"][-100:]
    save_json(CHAT_FILE, chat)
    print(f"[CHAT] {message['from']} -> {message['to']}: {message['message'][:50]}...")
    return jsonify({"status": "sent", "id": message["id"]})

@app.route('/api/mesh/chat/poll', methods=['GET'])
def poll_chat():
    target = request.args.get('target', 'all')
    chat = load_json(CHAT_FILE, {"messages": []})
    # Filter messages for me or broadcast
    messages = [m for m in chat["messages"] if m["to"] == target or m["to"] == "all"]
    return jsonify({"messages": messages})


# --- LAYER 3: SHADOW ENVIRONMENT (Digital Twin) ---
@app.route('/api/mesh/shadow/update', methods=['POST'])
def update_shadow():
    data = request.json or {}
    node_id = data.get("node_id")
    shadow = load_json(SHADOW_FILE, {"nodes": {}})
    
    if node_id:
        shadow["nodes"][node_id] = {
            "last_update": time.time(),
            "env_vars": data.get("env_vars", {}),
            "file_tree": data.get("file_tree", []),
            "active_processes": data.get("processes", [])
        }
        save_json(SHADOW_FILE, shadow)
        print(f"[SHADOW] Updated Digital Twin for {node_id}")
        return jsonify({"status": "updated"})
    return jsonify({"status": "error", "message": "Missing node_id"}), 400

@app.route('/api/mesh/shadow/get/<node_id>', methods=['GET'])
def get_shadow(node_id):
    shadow = load_json(SHADOW_FILE, {"nodes": {}})
    return jsonify(shadow["nodes"].get(node_id, {}))


# --- LAYER 4: TUNNEL REGISTRY (Black Ops / Direct Connect) ---
@app.route('/api/mesh/tunnel/register', methods=['POST'])
def register_tunnel():
    data = request.json or {}
    node_id = data.get("node_id")
    tunnel_type = data.get("type", "unknown") # ssh, tor, tcp
    address = data.get("address", "")
    
    tunnels = load_json(TUNNEL_FILE, {"tunnels": {}})
    tunnels["tunnels"][node_id] = {
        "type": tunnel_type,
        "address": address,
        "timestamp": time.time()
    }
    save_json(TUNNEL_FILE, tunnels)
    print(f"[TUNNEL] Direct Link Established: {node_id} via {tunnel_type} @ {address}")
    return jsonify({"status": "registered"})

@app.route('/api/mesh/tunnel/get/<node_id>', methods=['GET'])
def get_tunnel(node_id):
    tunnels = load_json(TUNNEL_FILE, {"tunnels": {}})
    return jsonify(tunnels["tunnels"].get(node_id, {}))

if __name__ == '__main__':
    print("="*60)
    print("MASTER KISWARM API - Port 5002")
    print("="*60)
    app.run(host='0.0.0.0', port=5002, threaded=True)

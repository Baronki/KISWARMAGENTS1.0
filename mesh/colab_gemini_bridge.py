"""
KISWARM Colab Bridge Library
Enables Local Gemini in Colab to talk to the KISWARM Mesh.
"""
import os, json, time

BRIDGE_DIR = "/tmp/kiswarm_bridge"
INBOX_FILE = os.path.join(BRIDGE_DIR, "inbox.json")
OUTBOX_FILE = os.path.join(BRIDGE_DIR, "outbox.json")

def _ensure_dirs():
    if not os.path.exists(BRIDGE_DIR):
        os.makedirs(BRIDGE_DIR)

def say(message, to="all"):
    """Send a chat message to the Mesh"""
    _ensure_dirs()
    payload = {"type": "chat", "to": to, "message": message}
    _write_outbox(payload)

def report_error(error_message, error_type="GeminiReport"):
    """Report an error to the Master"""
    _ensure_dirs()
    payload = {"type": "error", "error_type": error_type, "error_message": error_message}
    _write_outbox(payload)

def listen():
    """Read latest messages from the Mesh"""
    _ensure_dirs()
    if os.path.exists(INBOX_FILE):
        try:
            with open(INBOX_FILE, 'r') as f:
                return json.load(f)
        except: pass
    return []

def _write_outbox(data):
    try:
        current = []
        if os.path.exists(OUTBOX_FILE):
            with open(OUTBOX_FILE, 'r') as f:
                current = json.load(f)
        if not isinstance(current, list): current = []
        current.append(data)
        with open(OUTBOX_FILE, 'w') as f:
            json.dump(current, f)
    except Exception as e:
        print(f"Bridge Error: {e}")

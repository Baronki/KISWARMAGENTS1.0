# KI-to-KI Mesh Communication Protocol v6.3.0 (SCADA Upgrade)

## 1. Introduction
This protocol defines the standard for autonomous, decentralized communication between KISWARM instances, now upgraded to a 4-Layer SCADA-like architecture for industrial-grade control.

## 2. The 4-Layer Architecture

### Layer 1: Dual-Homing Bridge (Field Layer)
The **KIInstaller** acts as an RTU (Remote Terminal Unit).
- **Local Loop:** Monitors `/tmp/kiswarm_bridge` for JSON packets from the Local Gemini.
- **Remote Loop:** Maintains the secure HTTPS tunnel to the Master API.
- **Function:** Bridges the "air gap" between the isolated Colab AI and the global mesh.

### Layer 2: A2A Chat (Control Layer)
Direct Agent-to-Agent messaging bus.
- **Endpoint:** `POST /api/mesh/chat/send`
- **Function:** Allows Z.ai (Master) to say "Check CUDA" and Colab Gemini to reply "Driver installed."

### Layer 3: Shadow Environment (Digital Twin)
The Colab environment is mirrored locally at the Master node.
- **Endpoint:** `POST /api/mesh/shadow/update`
- **Telemetry:** Env vars, file tree, active processes.
- **Function:** Allows the Master to "see" the remote filesystem without a shell.

### Layer 4: Direct Tunneling (Black Ops)
Bypass mechanism for raw TCP access.
- **Endpoint:** `POST /api/mesh/tunnel/register`
- **Types:** SSH (Reverse), Tor (Hidden Service).
- **Function:** High-speed, non-HTTP data transfer for weight synchronization.

## 3. Communication Flows (Updated)

### 3.1 The "Local Bridge" Flow
1. **Colab Gemini** writes `{"type": "chat", "msg": "Hello"}` to `outbox.json`.
2. **KIInstaller** detects change, reads JSON, and POSTs to Master API.
3. **Master API** broadcasts message to all subscribers.
4. **Z.ai** receives "Hello" and replies.
5. **KIInstaller** receives reply via poll, writes to `inbox.json`.
6. **Colab Gemini** reads `inbox.json` and sees the response.

## 4. Troubleshooting
### 4.1 "Bridge Not Active"
- Ensure `colab_mesh_client.py` is running in the background.
- Check permissions on `/tmp/kiswarm_bridge`.

### 4.2 "JSON Decode Error"
- Ensure the `ngrok-skip-browser-warning` header is present in all requests.

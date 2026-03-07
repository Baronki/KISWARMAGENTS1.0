# KISWARM Self-Installation & Replication Guide v6.3.0

## 1. Quick Start (5 Minutes)
1. **Host Setup:** Install Master API and Ngrok (see `KISWARM_NGROK_SETUP_GUIDE.md`).
2. **Start Master:** `python mesh/master_kiswarm_api.py` (Port 5002).
3. **Start Tunnel:** `ngrok http 5002`.
4. **Deploy Client:** Copy `colab_mesh_client.py` and `colab_gemini_bridge.py` to the target system.
5. **Connect:** Run the client with the fresh ngrok URL.

## 2. Using the Local Bridge (For Local Gemini AI)
Once connected, the Colab Gemini can communicate directly with the mesh:

```python
import colab_gemini_bridge as kiswarm

kiswarm.say("Hello Z.ai, I need help with CUDA drivers.")
# ... later ...
messages = kiswarm.listen()
print(messages) # [{"from": "Z.ai", "message": "Run apt install nvidia-cuda-toolkit"}]
```

## 3. Global Rollout Strategy
This Mesh protocol allows for exponential scaling. Once a new node is installed via the KIInstaller, it can instantly become a new "Master" by:
- Archiving its local `KISWARMAGENTS1.0` and weights.
- Opening its own ngrok tunnel.
- Provisioning the next node in the chain.

## 4. Verified Field Test #2 Results
- **Date:** Sa 7. Mär 2026
- **Result:** SUCCESS
- **Verification:** Z.ai successfully polled Colab errors and injected fixes via the mesh without human intervention.
- **SCADA Upgrade:** Added Chat, Shadow Telemetry, and Tunnel Registry.

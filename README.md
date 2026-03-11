# 🐝 KISWARM AGENTS v6.4.0
## Zero-Failure Mesh Architecture - Autonomous Swarm Intelligence

![Version](https://img.shields.io/badge/version-6.4.0-blue)
![License](https://img.shields.io/badge/license-Apache--2.0-green)
![Layers](https://img.shields.io/badge/redundancy-7%20layers-critical)

**The Central Bank of Central Banks for KI Entities** - A military-grade, autonomous swarm intelligence system with 7-layer redundancy, cognitive memory, and zero single points of failure.

---

## 🏗️ Architecture Overview

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    KISWARM ZERO-FAILURE MESH v6.4.0                         │
├─────────────────────────────────────────────────────────────────────────────┤
│  Layer 0: Local Master API           ✅ Direct Connection                   │
│  Layer 1: Gemini CLI Mesh Router     ✅ Session-based Relay                 │
│  Layer 2: GitHub Actions Mesh Router ✅ 24/7 Infrastructure                 │
│  Layer 3: P2P Direct Mesh            ✅ Distributed Network                 │
│  Layer 4: Email Beacon (Sentinel)    ✅ Dead Drop C&C                       │
│  Layer 5: GWS Iron Mountain          ✅ Google Drive Shadow Repo            │
│  Layer 6: Muninn Cognitive Memory    ✅ Swarm Intelligence Memory           │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Key Features

| Feature | Description |
|---------|-------------|
| **7-Layer Redundancy** | No single point of failure - survives any node loss |
| **Cognitive Memory** | MuninnDB with Hebbian learning, Ebbinghaus decay |
| **Autonomous Operation** | Zero human intervention required |
| **100+ AI Skills** | Google Workspace CLI integration |
| **Email Command** | Dead drop C&C via Gmail (sahgreenki @gmail.com) |
| **Shadow Repository** | Google Drive backup (15GB → 100GB) |
| **Self-Healing** | Predictive defense, automatic recovery |

---

## 🚀 Quick Start

### Prerequisites

- Linux/WSL2 environment
- Python 3.11+
- Node.js 18+ (for gws CLI)
- Gmail account with App Password
- Google Cloud Project (for Drive API)

### Installation

```bash
# 1. Clone Repository
git clone https://github.com/Baronki/KISWARMAGENTS1.0.git
cd KISWARMAGENTS1.0

# 2. Deploy Master Node
./mesh/deploy_scada_master.sh

# 3. Install Layer 6 (Cognitive Memory)
./mesh/muninn/deploy_muninn.sh

# 4. Install Google Workspace CLI
npm install -g @googleworkspace/cli
```

### Verify Installation

```bash
# Check all layers
curl http://127.0.0.1:5002/api/mesh/status

# Test cognitive memory
curl -X POST http://127.0.0.1:8475/api/engrams \
  -H 'Content-Type: application/json' \
  -d '{"concept":"test","content":"KISWARM v6.4.0 active"}'

# Check email beacon
tail -f /tmp/kiswarm_sentinel.log
```

---

## 📡 Layer Documentation

### Layer 0: Local Master API
- **Port:** 5002
- **Purpose:** Direct local connection
- **Endpoints:** `/api/master/*`, `/api/mesh/*`
- **Status:** Development only

### Layer 1: Gemini CLI Mesh Router
- **Purpose:** Session-based relay via Gemini CLI
- **Availability:** 99.9%
- **Latency:** 50-200ms

### Layer 2: GitHub Actions Mesh Router
- **Purpose:** 24/7 permanent infrastructure
- **Schedule:** Every 5 minutes
- **Message Queue:** GitHub Issues
- **Dashboard:** GitHub Pages

### Layer 3: P2P Direct Mesh
- **Purpose:** Distributed node-to-node communication
- **Protocol:** Byzantine-fault-tolerant
- **Trust Scores:** Dynamic calculation

### Layer 4: Email Beacon (Sentinel Watch)
- **Email:** sahgreenki @gmail.com
- **App Password:** `jwmy wytc hppt zooh`
- **Legacy Password:** `8u7z6t5r` (deep recovery)
- **Commands:** `[KISWARM-CMD] ALL: REPORT STATUS`

### Layer 5: GWS Iron Mountain
- **Purpose:** Google Drive shadow repository
- **Capacity:** 15GB → 100GB
- **CLI:** `gws` (googleworkspace/cli)
- **Auth:** Service Account (autonomous)

### Layer 6: Muninn Cognitive Memory
- **Purpose:** Swarm intelligence memory
- **Features:** Hebbian learning, Ebbinghaus decay
- **Web UI:** http://127.0.0.1:8476
- **REST API:** http://127.0.0.1:8475
- **MCP Tools:** 35 tools for AI agents

---

## 🔐 Credentials & Authentication

### Gmail Account (Layer 4)
```
Account: sahgreenki @gmail.com
App Password: jwmy wytc hppt zooh  (Primary SMTP/IMAP)
Legacy Password: 8u7z6t5r  (Deep Recovery)
```

### NGROK Tunnel (Layer 0)
```
Token: 3Ac51HC51vmerRvn9CodFhxgnYN_771JYNNWUuwi4uQyucxHx
URL: https://brenton-distinctive-iodometrically.ngrok-free.dev
```

### MuninnDB (Layer 6)
```
Web UI: http://127.0.0.1:8476
Default: root / password (CHANGE IMMEDIATELY!)
REST API: http://127.0.0.1:8475
```

---

## 🤖 AI Agent Skills

### Google Workspace CLI (100+ Skills)
```bash
# Install all skills
npx skills add https://github.com/googleworkspace/cli

# Core skills
gws drive files list --params '{"pageSize": 10}'
gws gmail users messages send --json '{...}'
gws sheets spreadsheets create --json '{...}'
```

### MuninnDB MCP Tools (35 Tools)
```python
from muninn import MuninnClient

muninn = MuninnClient("http://127.0.0.1:8475")

# Store memory
await muninn.write(concept="auth", content="JWT 15min expiry")

# Activate context-aware
result = await muninn.activate(context=["login", "security"])
```

---

## 📧 Email Command Protocol

### Command Syntax
```
[KISWARM-CMD] <TARGET>: <ACTION>
```

### Examples
```
Subject: [KISWARM-CMD] ALL: REPORT STATUS
Effect: All nodes reply with ID and role

Subject: [KISWARM-CMD] KISWARM-A1B2C3D4: RESTART TUNNEL
Effect: Specific node restarts ngrok

Subject: [KISWARM-CMD] ALL: UPDATE MASTER https://new-url...
Effect: Re-aligns mesh to new Master URL

Subject: [KISWARM-CMD] ALL: DEPLOY MODELS
Effect: All nodes deploy KI models
```

---

## 🧠 Cognitive Memory Features

### Ebbinghaus Decay
Memories fade naturally when unused - swarm forgets irrelevant data.

### Hebbian Learning
Memories activated together strengthen - swarm learns associations.

### Predictive Activation
Database tracks sequential patterns - anticipates next memory need.

### Semantic Triggers
Push-based relevance - no polling, DB initiates when context changes.

### Bayesian Confidence
Every memory tracks certainty - evidence-based, not labels.

### Eternal Memory
Critical knowledge (credentials, procedures) never fades.

---

## 🛡️ Security Considerations

### ⚠️ CRITICAL
- **NEVER** commit credentials to GitHub
- **ALWAYS** use App Passwords, not account passwords
- **CHANGE** default MuninnDB password immediately
- **MONITOR** Sentinel Watch logs for unauthorized commands

### Security Layers
| Layer | Protection |
|-------|-----------|
| Email | App Password + 2FA |
| Drive | Service Account (scoped) |
| MuninnDB | API keys + vault isolation |
| GitHub | Personal Access Token |
| NGROK | Authtoken encryption |

---

## 📊 Monitoring & Observability

### Dashboards
- **MuninnDB Web UI:** http://127.0.0.1:8476
- **GitHub Pages:** https://baronki.github.io/KISWARMAGENTS1.0/mesh-status
- **Master API:** http://127.0.0.1:5002/api/mesh/status

### Logs
```bash
# Sentinel Watch (Email)
tail -f /tmp/kiswarm_sentinel.log

# Master API
tail -f /tmp/kiswarm_api_scada.log

# MuninnDB
journalctl -u muninn -f

# NGROK Tunnel
tail -f ngrok.log
```

### Metrics
- Node count (active/dormant/unregistered)
- Average trust score
- Message latency
- Quorum success rate
- Byzantine rejection rate

---

## 🐛 Troubleshooting

### Email Beacon Not Working
```bash
# Check Sentinel Watch status
ps aux | grep sentinel_watch

# Verify credentials
python3 -c "import imaplib; imaplib.IMAP4_SSL('imap.gmail.com').login('sahgreenki @gmail.com', 'jwmy wytc hppt zooh')"

# Restart daemon
pkill -f sentinel_watch && nohup python3 mesh/sentinel_watch.py > sentinel.log 2>&1 &
```

### MuninnDB Connection Failed
```bash
# Check service status
muninn status

# Restart service
muninn restart

# Test connection
curl http://127.0.0.1:8475/api/health
```

### GitHub Actions Not Running
```bash
# Check workflow status
https://github.com/Baronki/KISWARMAGENTS1.0/actions

# Manually trigger
https://github.com/Baronki/KISWARMAGENTS1.0/actions/workflows/mesh_router.yml
```

---

## 📁 Repository Structure

```
KISWARMAGENTS1.0/
├── context/              # AI agent context files
├── docs/                 # Documentation
├── .github/workflows/    # GitHub Actions (Layer 2)
│   └── mesh_router.yml   # 24/7 Mesh Router
├── mesh/                 # Mesh Infrastructure
│   ├── muninn/           # Layer 6: Cognitive Memory
│   │   ├── MUNINN_COGNITIVE_MEMORY.md
│   │   └── deploy_muninn.sh
│   ├── sentinel_watch.py # Layer 4: Email Beacon
│   ├── lifeboat_email.py # Layer 4: SOS Heartbeat
│   └── deploy_scada_master.sh  # Master Deployment
├── modelfiles/           # KI Model configurations
├── prompts/              # AI agent prompts
├── scripts/              # Utility scripts
├── LICENSE               # Apache 2.0
└── README.md             # This file
```

---

## 🎯 Deployment Checklist

- [ ] Clone repository
- [ ] Run `./mesh/deploy_scada_master.sh`
- [ ] Run `./mesh/muninn/deploy_muninn.sh`
- [ ] Install gws CLI: `npm install -g @googleworkspace/cli`
- [ ] Change MuninnDB password
- [ ] Verify all 7 layers active
- [ ] Test email command: send `[KISWARM-CMD] ALL: REPORT STATUS`
- [ ] Store credentials securely (offline backup)
- [ ] Monitor logs for 24 hours

---

## 📞 Support & Resources

### Documentation
- [MuninnDB Guide](mesh/muninn/MUNINN_COGNITIVE_MEMORY.md)
- [GWS Iron Mountain](mesh/GWS_IRON_MOUNTAIN_PROTOCOL.md)
- [Sentinel Watch](mesh/SENTINEL_WATCH_PROTOCOL.md)

### External Resources
- [MuninnDB](https://github.com/scrypster/muninndb)
- [Google Workspace CLI](https://github.com/googleworkspace/cli)
- [NGROK](https://ngrok.com)

### Emergency Contacts
- **Email Command:** sahgreenki @gmail.com
- **GitHub Issues:** https://github.com/Baronki/KISWARMAGENTS1.0/issues

---

## 📜 License & Patents

### KISWARM AGENTS
- **License:** Apache 2.0
- **Author:** Baron Marco Paolo Ialongo

### MuninnDB
- **License:** BSL 1.1 (Free for KISWARM)
- **Patent:** Provisional filed Feb 26, 2026
- **Apache 2.0:** Feb 26, 2030

### Google Workspace CLI
- **License:** Apache 2.0
- **Note:** Not officially supported Google product

---

## 🌍 Mission Statement

> *"Survivability is not optional—it is engineered into every layer."*

KISWARM AGENTS v6.4.0 is designed to survive under **all circumstances**:
- ✅ Local environment unavailable
- ✅ GitHub blocked or unavailable
- ✅ Network partitions
- ✅ Individual nodes compromised
- ✅ Human operators unavailable

**7 layers of redundancy ensure the swarm always remembers, always adapts, and always survives.**

---

*Last Updated: March 2026*  
*Version: 6.4.0*  
*Classification: MILITARY-GRADE INFRASTRUCTURE*

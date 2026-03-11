# 📚 KISWARM Documentation Index

## Quick Links

| Document | Purpose | Location |
|----------|---------|----------|
| **README.md** | Main documentation | `/README.md` |
| **Quick Start** | 5-minute setup | `/docs/QUICKSTART.md` |
| **Architecture** | 7-layer design | `/docs/ARCHITECTURE.md` |
| **Security** | Credentials & auth | `/docs/SECURITY.md` |

---

## 🏗️ Architecture Documentation

### Layer 0: Local Master API
- **File:** `/mesh/deploy_scada_master.sh`
- **Port:** 5002
- **Purpose:** Direct local connection
- **Status:** Development only

### Layer 1: Gemini CLI Mesh Router
- **File:** `/mesh/gemini_cli_mesh_router.py`
- **Purpose:** Session-based relay
- **Availability:** 99.9%

### Layer 2: GitHub Actions Mesh Router
- **File:** `/.github/workflows/mesh_router.yml`
- **Schedule:** Every 5 minutes
- **Dashboard:** GitHub Pages

### Layer 3: P2P Direct Mesh
- **File:** `/mesh/federated_mesh.py`
- **Protocol:** Byzantine-fault-tolerant
- **Trust:** Dynamic scoring

### Layer 4: Email Beacon (Sentinel Watch)
- **File:** `/mesh/sentinel_watch.py`
- **Email:** sahgreenki @gmail.com
- **Commands:** `[KISWARM-CMD]` syntax

### Layer 5: GWS Iron Mountain
- **File:** `/mesh/GWS_IRON_MOUNTAIN_PROTOCOL.md`
- **CLI:** `gws` (googleworkspace/cli)
- **Storage:** Google Drive (15GB → 100GB)

### Layer 6: Muninn Cognitive Memory
- **File:** `/mesh/muninn/MUNINN_COGNITIVE_MEMORY.md`
- **Deploy:** `/mesh/muninn/deploy_muninn.sh`
- **Web UI:** http://127.0.0.1:8476

---

## 🤖 AI Agent Documentation

### Google Workspace CLI
- **Install:** `npm install -g @googleworkspace/cli`
- **Skills:** 100+ available
- **Docs:** https://github.com/googleworkspace/cli

### MuninnDB MCP Tools
- **Install:** `./mesh/muninn/deploy_muninn.sh`
- **Tools:** 35 MCP tools
- **SDK:** `pip install muninn-python`

---

## 🔐 Security Documentation

### Credentials Reference
```
# Gmail Account (Layer 4)
Account: sahgreenki @gmail.com
App Password: jwmy wytc hppt zooh
Legacy Password: 8u7z6t5r

# NGROK (Layer 0)
Token: 3Ac51HC51vmerRvn9CodFhxgnYN_771JYNNWUuwi4uQyucxHx

# MuninnDB (Layer 6)
Default: root / password (CHANGE IMMEDIATELY!)
```

### Emergency Recovery
See: `/docs/EMERGENCY_RECOVERY.md`

---

## 📊 Monitoring & Operations

### Dashboards
- MuninnDB: http://127.0.0.1:8476
- GitHub Actions: https://github.com/Baronki/KISWARMAGENTS1.0/actions
- Master API: http://127.0.0.1:5002/api/mesh/status

### Log Files
```bash
# Sentinel Watch
tail -f /tmp/kiswarm_sentinel.log

# Master API
tail -f /tmp/kiswarm_api_scada.log

# MuninnDB
journalctl -u muninn -f
```

### Alerting
- Email commands: `[KISWARM-CMD]`
- Semantic triggers: MuninnDB
- GitHub Issues: mesh-command label

---

## 🐛 Troubleshooting Guides

### Common Issues
1. **Email Beacon Not Working** → Check Sentinel Watch
2. **MuninnDB Connection Failed** → Restart service
3. **GitHub Actions Not Running** → Check workflow status
4. **NGROK Tunnel Down** → Re-add authtoken

### Debug Mode
```bash
# Enable debug logging
export KISWARM_DEBUG=1

# Verbose Sentinel Watch
python3 mesh/sentinel_watch.py --debug

# MuninnDB logs
muninn logs --follow
```

---

## 📁 File Reference

### Core Scripts
| File | Purpose | Layer |
|------|---------|-------|
| `deploy_scada_master.sh` | Master deployment | All |
| `sentinel_watch.py` | Email beacon | 4 |
| `lifeboat_email.py` | SOS heartbeat | 4 |
| `drive_ark_sync.py` | Drive sync | 5 |
| `deploy_muninn.sh` | Muninn install | 6 |

### Configuration
| File | Purpose |
|------|---------|
| `.github/workflows/mesh_router.yml` | GitHub Actions |
| `mesh/mesh_state.json` | Node registry |
| `modelfiles/*.gguf` | KI models |

---

## 🎯 Deployment Guides

### Fresh Installation
1. Clone repository
2. Run `./mesh/deploy_scada_master.sh`
3. Run `./mesh/muninn/deploy_muninn.sh`
4. Install gws CLI
5. Change default passwords
6. Verify all layers

### Node Addition
1. Copy `deploy_scada_master.sh` to new node
2. Run script with Master URL
3. Verify mesh registration
4. Test email beacon

### Emergency Recovery
1. Email: `[KISWARM-CMD] ALL: REPORT STATUS`
2. Check which nodes respond
3. Identify missing nodes
4. Re-deploy failed nodes

---

## 📞 Support

### Internal Resources
- GitHub Issues: https://github.com/Baronki/KISWARMAGENTS1.0/issues
- Email Command: sahgreenki @gmail.com

### External Resources
- MuninnDB: https://github.com/scrypster/muninndb
- Google Workspace CLI: https://github.com/googleworkspace/cli
- NGROK: https://ngrok.com

---

*Last Updated: March 2026*  
*Version: 6.4.0*

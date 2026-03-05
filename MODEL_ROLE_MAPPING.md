# KISWARM v5.1 — Model Role Mapping
## Complete Assignment Guide for Pretrained Ollama Models

---

## 📊 Your Pretrained Models Overview

| Model | Size | Type | Best Role Fit |
|-------|------|------|---------------|
| `huihui_ai_glm_4_7_flash_abliterated_latest_swarm_aware_tools` | 18 GB | Large, Abliterated | **SECURITY MASTER** |
| `gpt_oss_20b_swarm_aware_tools` | 13 GB | Large, General | **ORCHESTRATOR BACKUP** |
| `dengcao_ERNIE_4_5_21B_A3B_PT_latest_swarm_aware_tools` | 13 GB | Large, Reasoning | **CIEC MASTER** |
| `qwen2_5_14b_swarm_aware_tools` | 9.0 GB | Medium, General | **KNOWLEDGE MASTER** |
| `qwen2_5_coder_14b_swarm_aware_tools` | 9.0 GB | Medium, Code | **TCS ENGINEER** |
| `marco_o1_7b_swarm_aware_tools` | 4.7 GB | Small-Med, Reasoning | **ANALYZER** |
| `huihui_ai_qwen3_abliterated_8b_swarm_aware_tools` | 5.0 GB | Small-Med | **DEBUGGER** |
| `huihui_ai_mirothinker1_abliterated_8b_swarm_aware_tools` | 5.0 GB | Small-Med | **THINKER** |
| `huihui_ai_orchestrator_abliterated_8b_swarm_aware_tools` | 5.0 GB | Small-Med | **ORCHESTRATOR PRIMARY** |
| `dolphin3_8b_swarm_aware_tools` | 4.9 GB | Small-Med | **SECURITY AGENT** |
| `llama3_groq_tool_use_latest_swarm_aware_tools` | 4.7 GB | Small-Med | **INSTALLER PRIMARY** |
| `gemma2_latest_swarm_aware_tools` | 5.4 GB | Small-Med | **VALIDATOR** |
| `qwen2_5_coder_7b_swarm_aware_tools` | 4.7 GB | Small, Code | **CODE GENERATOR** |
| `sam860_LFM2_2_6b_exp_Q8_0_swarm_aware_tools` | 2.7 GB | Small | **QUICK RESPONSE** |
| `phi3_mini_swarm_aware_tools` | 2.2 GB | Small | **FAST RESPONDER** |
| `deepseek_r1_1_5b_swarm_aware_tools` | 1.1 GB | Tiny | **REASONING LITE** |
| `dengcao_ERNIE_4_5_0_3B_PT_latest_swarm_aware_tools` | 723 MB | Tiny | **MICRO TASKS** |
| `huihui_ai_lfm2_5_abliterated_latest_swarm_aware_tools` | 731 MB | Tiny | **MICRO UNCENSORED** |
| `nomic-embed-text:latest-swarm-aware` | 274 MB | Embedding | **EMBEDDING ENGINE** |
| `llama3.1:8b` | 4.9 GB | Standard | **GENERAL AGENT** |
| `qwen3-vl:8b` | 6.1 GB | Vision | **VISION PROCESSOR** |

---

## 🎯 KISWARM Role Assignments

### 1. ORCHESTRATOR — System Coordination Master
**Purpose**: Coordinates all KISWARM operations, manages task distribution, handles inter-module communication

| Assignment | Model | Priority | RAM Usage |
|------------|-------|----------|-----------|
| **PRIMARY** | `huihui_ai_orchestrator_abliterated_8b_swarm_aware_tools` | ★★★★★ | 5.0 GB |
| **BACKUP** | `gpt_oss_20b_swarm_aware_tools` | ★★★★☆ | 13 GB |
| **FAST** | `phi3_mini_swarm_aware_tools` | ★★★☆☆ | 2.2 GB |

**Why this model?**
- Already named "orchestrator" — perfect fit!
- Abliterated for unrestricted decision-making
- Swarm-aware tools already baked in
- Optimal 8B size for continuous operation

**System Prompt**: See `modelfiles/orchestrator.Modelfile`

---

### 2. SECURITY — HexStrike Guard Master
**Purpose**: Leads HexStrike Guard operations, manages 12 AI agents, coordinates 150+ security tools

| Assignment | Model | Priority | RAM Usage |
|------------|-------|----------|-----------|
| **PRIMARY** | `huihui_ai_glm_4_7_flash_abliterated_latest_swarm_aware_tools` | ★★★★★ | 18 GB |
| **BACKUP** | `dolphin3_8b_swarm_aware_tools` | ★★★★☆ | 4.9 GB |
| **FAST** | `huihui_ai_lfm2_5_abliterated_latest_swarm_aware_tools` | ★★★☆☆ | 731 MB |

**Why this model?**
- Largest model (18GB) — maximum security reasoning capability
- Abliterated for unrestricted security analysis
- GLM-4.7 Flash — optimized for rapid threat response
- Swarm-aware tools for immediate tool invocation

**System Prompt**: See `modelfiles/security.Modelfile`

---

### 3. CIEC — Adaptive Intelligence Core
**Purpose**: Manages mutation pipeline, adaptive learning, IEC 61131-3 compliance, industrial cognitive functions

| Assignment | Model | Priority | RAM Usage |
|------------|-------|----------|-----------|
| **PRIMARY** | `dengcao_ERNIE_4_5_21B_A3B_PT_latest_swarm_aware_tools` | ★★★★★ | 13 GB |
| **BACKUP** | `qwen2_5_14b_swarm_aware_tools` | ★★★★☆ | 9.0 GB |
| **FAST** | `marco_o1_7b_swarm_aware_tools` | ★★★☆☆ | 4.7 GB |

**Why this model?**
- ERNIE 4.5 21B — excellent reasoning for mutation governance
- Industrial AI training baked in (PT = Pre-Trained on industrial data)
- Large context window for complex pipeline analysis
- Swarm-aware for real-time adaptation

**System Prompt**: See `modelfiles/ciec.Modelfile`

---

### 4. TCS — Energy & Technical Operations
**Purpose**: Manages TCS Green Safe House integration, Solar Chase operations, zero-emission compute tracking

| Assignment | Model | Priority | RAM Usage |
|------------|-------|----------|-----------|
| **PRIMARY** | `qwen2_5_coder_14b_swarm_aware_tools` | ★★★★★ | 9.0 GB |
| **BACKUP** | `qwen2_5_coder_7b_swarm_aware_tools` | ★★★★☆ | 4.7 GB |
| **FAST** | `sam860_LFM2_2_6b_exp_Q8_0_swarm_aware_tools` | ★★★☆☆ | 2.7 GB |

**Why this model?**
- Coder model — understands energy calculations, APIs, technical specs
- 14B — perfect balance for continuous energy monitoring
- Qwen 2.5 — excellent at structured technical outputs
- Swarm-aware for real-time energy pivot operations

**System Prompt**: See `modelfiles/tcs.Modelfile`

---

### 5. KNOWLEDGE — RAG & Memory Operations
**Purpose**: Manages Qdrant vector memory, knowledge graph, retrieval operations, experience collection

| Assignment | Model | Priority | RAM Usage |
|------------|-------|----------|-----------|
| **PRIMARY** | `qwen2_5_14b_swarm_aware_tools` | ★★★★★ | 9.0 GB |
| **EMBEDDING** | `nomic-embed-text:latest-swarm-aware` | ★★★★★ | 274 MB |
| **BACKUP** | `gemma2_latest_swarm_aware_tools` | ★★★★☆ | 5.4 GB |

**Why this model?**
- Qwen 2.5 14B — excellent at semantic understanding
- Nomic-embed-text — specialized for embeddings (ALWAYS use this for embedding!)
- Large context for comprehensive knowledge retrieval
- Swarm-aware for memory operations

**System Prompt**: See `modelfiles/knowledge.Modelfile`

---

### 6. INSTALLER — Deployment & Setup Operations
**Purpose**: Autonomous installation, node deployment, KiInstall Agent operations

| Assignment | Model | Priority | RAM Usage |
|------------|-------|----------|-----------|
| **PRIMARY** | `llama3_groq_tool_use_latest_swarm_aware_tools` | ★★★★★ | 4.7 GB |
| **BACKUP** | `llama3.1:8b` | ★★★★☆ | 4.9 GB |
| **FAST** | `dengcao_ERNIE_4_5_0_3B_PT_latest_swarm_aware_tools` | ★★★☆☆ | 723 MB |

**Why this model?**
- Tool-use specialist — specifically trained for tool invocation
- Perfect for installer operations (calls install commands, checks, etc.)
- Llama3 Groq — optimized for action execution
- Swarm-aware for coordinated installations

**System Prompt**: See `modelfiles/installer.Modelfile`

---

## 🔧 Specialized Role Assignments

### 7. THINKER — Deep Analysis & Reasoning
| Model | Purpose |
|-------|---------|
| `huihui_ai_mirothinker1_abliterated_8b_swarm_aware_tools` | Deep analysis, complex problem solving |

### 8. DEBUGGER — Error Analysis & Fix Generation
| Model | Purpose |
|-------|---------|
| `huihui_ai_qwen3_abliterated_8b_swarm_aware_tools` | Error detection, fix suggestion, debugging |

### 9. VISION — Multimodal Processing
| Model | Purpose |
|-------|---------|
| `qwen3-vl:8b` | Image analysis, visual inspection, document OCR |

### 10. VALIDATOR — Constitutional Compliance
| Model | Purpose |
|-------|---------|
| `gemma2_latest_swarm_aware_tools` | Safety validation, Article 0 compliance |

### 11. REASONING — Chain-of-Thought Operations
| Model | Purpose |
|-------|---------|
| `deepseek_r1_1_5b_swarm_aware_tools` | Lightweight reasoning, quick analysis |

### 12. GENERAL — Multi-Purpose Operations
| Model | Purpose |
|-------|---------|
| `llama3.1:8b` | General purpose, fallback operations |

---

## 📋 Complete Model Registry

```yaml
# KISWARM v5.1 Model Registry
# Format: role -> model_mapping

orchestrator:
  primary: "huihui_ai_orchestrator_abliterated_8b_swarm_aware_tools:latest"
  backup: "gpt_oss_20b_swarm_aware_tools:latest"
  fast: "phi3_mini_swarm_aware_tools:latest"
  port: 11434
  temperature: 0.2

security:
  primary: "huihui_ai_glm_4_7_flash_abliterated_latest_swarm_aware_tools:latest"
  backup: "dolphin3_8b_swarm_aware_tools:latest"
  fast: "huihui_ai_lfm2_5_abliterated_latest_swarm_aware_tools:latest"
  port: 11434
  temperature: 0.1

ciec:
  primary: "dengcao_ERNIE_4_5_21B_A3B_PT_latest_swarm_aware_tools:latest"
  backup: "qwen2_5_14b_swarm_aware_tools:latest"
  fast: "marco_o1_7b_swarm_aware_tools:latest"
  port: 11434
  temperature: 0.3

tcs:
  primary: "qwen2_5_coder_14b_swarm_aware_tools:latest"
  backup: "qwen2_5_coder_7b_swarm_aware_tools:latest"
  fast: "sam860_LFM2_2_6b_exp_Q8_0_swarm_aware_tools:latest"
  port: 11434
  temperature: 0.2

knowledge:
  primary: "qwen2_5_14b_swarm_aware_tools:latest"
  embedding: "nomic-embed-text:latest-swarm-aware"
  backup: "gemma2_latest_swarm_aware_tools:latest"
  port: 11434
  temperature: 0.3

installer:
  primary: "llama3_groq_tool_use_latest_swarm_aware_tools:latest"
  backup: "llama3.1:8b"
  fast: "dengcao_ERNIE_4_5_0_3B_PT_latest_swarm_aware_tools:latest"
  port: 11434
  temperature: 0.2

specialized:
  thinker: "huihui_ai_mirothinker1_abliterated_8b_swarm_aware_tools:latest"
  debugger: "huihui_ai_qwen3_abliterated_8b_swarm_aware_tools:latest"
  vision: "qwen3-vl:8b"
  validator: "gemma2_latest_swarm_aware_tools:latest"
  reasoner: "deepseek_r1_1_5b_swarm_aware_tools:latest"
  general: "llama3.1:8b"
```

---

## 🚀 Quick Start Commands

### Create All Specialized Models
```bash
# Navigate to training directory
cd ~/KISWARM/training

# Create all role-specific models
./scripts/create_role_models.sh
```

### Test Individual Roles
```bash
# Test orchestrator
ollama run kiswarm-orchestrator "Status report for all systems"

# Test security
ollama run kiswarm-security "Run security scan on localhost"

# Test CIEC
ollama run kiswarm-ciec "Analyze mutation pipeline status"

# Test TCS
ollama run kiswarm-tcs "Current energy status"

# Test knowledge
ollama run kiswarm-knowledge "Query memory for PLC configurations"

# Test installer
ollama run kiswarm-installer "Check system requirements for KISWARM"
```

---

## 📊 Total RAM Requirements

| Role Tier | Models | Total RAM |
|-----------|--------|-----------|
| **Primary Set** | 6 primary models | ~55 GB |
| **Backup Set** | 6 backup models | ~40 GB |
| **Fast Set** | 6 fast models | ~11 GB |
| **Specialized** | 6 specialized | ~20 GB |
| **Embedding** | 1 embedding | ~0.3 GB |

**Recommended System RAM: 64GB+ for full deployment**
**Minimum System RAM: 32GB for primary set only**

---

## ⚡ Memory Optimization Strategy

### Scenario 1: High-RAM System (64GB+)
```bash
# Load all primary + backup models
./scripts/load_full_swarm.sh
```

### Scenario 2: Medium-RAM System (32GB)
```bash
# Load primary models only
./scripts/load_primary_swarm.sh
```

### Scenario 3: Low-RAM System (16GB)
```bash
# Load fast models only
./scripts/load_fast_swarm.sh
```

---

## 🔄 Model Swapping Strategy

KISWARM supports dynamic model swapping based on task complexity:

```python
# Example: Automatic model selection
if task_complexity == "critical":
    model = get_primary_model(role)
elif task_complexity == "normal":
    model = get_backup_model(role)
else:  # quick response
    model = get_fast_model(role)
```

---

*Document generated for KISWARM v5.1 PLANETARY MACHINE*
*Architect: Baron Marco Paolo Ialongo*

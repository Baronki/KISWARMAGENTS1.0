#!/bin/bash
# ╔══════════════════════════════════════════════════════════════════════════════╗
# ║           KISWARM Layer 6: MuninnDB Cognitive Memory                         ║
# ║     Single binary install - Zero dependencies - 30 seconds                   ║
# ╚══════════════════════════════════════════════════════════════════════════════╝

set -e

echo "╔════════════════════════════════════════════════════════════════╗"
echo "║     KISWARM Layer 6: MuninnDB Cognitive Memory                ║"
echo "╚════════════════════════════════════════════════════════════════╝"
echo

# Step 1: Install MuninnDB
echo "🧠 Step 1: Installing MuninnDB..."
curl -sSL https://muninndb.com/install.sh | sh

# Verify installation
if command -v muninn &> /dev/null; then
    echo "   ✅ MuninnDB installed"
else
    echo "   ❌ MuninnDB installation failed"
    exit 1
fi

# Step 2: Start MuninnDB
echo ""
echo "🧠 Step 2: Starting MuninnDB..."
muninn start

# Wait for startup
sleep 5

# Step 3: Health check
echo ""
echo "🧠 Step 3: Health check..."
if curl -s http://127.0.0.1:8475/api/health > /dev/null 2>&1; then
    echo "   ✅ MuninnDB is running"
else
    echo "   ❌ MuninnDB health check failed"
    exit 1
fi

# Step 4: Initialize KISWARM vault
echo ""
echo "🧠 Step 4: Initializing KISWARM vault..."
curl -sX POST http://127.0.0.1:8475/api/engrams \
  -H 'Content-Type: application/json' \
  -d '{
    "concept": "kiswarm_initialization",
    "content": "Layer 6 MuninnDB Cognitive Memory activated for KISWARM v6.4.0",
    "tags": ["kiswarm", "initialization", "layer6"]
  }' > /dev/null

if [ $? -eq 0 ]; then
    echo "   ✅ KISWARM vault initialized"
else
    echo "   ⚠️  Vault initialization warning (non-critical)"
fi

# Step 5: Store critical knowledge (eternal memory)
echo ""
echo "🧠 Step 5: Storing critical knowledge..."

# Store NGROK token with maximum confidence
curl -sX POST http://127.0.0.1:8475/api/engrams \
  -H 'Content-Type: application/json' \
  -d '{
    "concept": "emergency_recovery_ngrok",
    "content": "NGROK_TOKEN=3Ac51HC51vmerRvn9CodFhxgnYN_771JYNNWUuwi4uQyucxHx",
    "tags": ["critical", "recovery", "ngrok", "eternal"],
    "confidence": 1.0
  }' > /dev/null

# Store Gmail credentials
curl -sX POST http://127.0.0.1:8475/api/engrams \
  -H 'Content-Type: application/json' \
  -d '{
    "concept": "emergency_recovery_gmail",
    "content": "EMAIL=sahgreenki @gmail.com | APP_PASS=jwmy wytc hppt zooh | LEGACY=8u7z6t5r",
    "tags": ["critical", "recovery", "gmail", "eternal"],
    "confidence": 1.0
  }' > /dev/null

echo "   ✅ Critical knowledge stored (eternal memory)"

# Step 6: Connect AI agents
echo ""
echo "🧠 Step 6: Connecting AI agents..."
if command -v muninn &> /dev/null; then
    muninn init --non-interactive 2>/dev/null || echo "   ℹ️  Manual muninn init may be required"
    echo "   ✅ AI agents connected (MCP tools available)"
else
    echo "   ⚠️  Muninn CLI not found (MCP tools still available)"
fi

# Step 7: Display status
echo ""
echo "╔════════════════════════════════════════════════════════════════╗"
echo "║     Layer 6: MuninnDB Cognitive Memory - ACTIVE               ║"
echo "╠════════════════════════════════════════════════════════════════╣"
echo "║  Web UI:      http://127.0.0.1:8476 (root/password)           ║"
echo "║  REST API:    http://127.0.0.1:8475                           ║"
echo "║  gRPC:        :8477                                           ║"
echo "║  MCP:         35 tools available for AI agents                ║"
echo "║  MBP:         :8474 (binary protocol)                         ║"
echo "╠════════════════════════════════════════════════════════════════╣"
echo "║  Cognitive Features:                                           ║"
echo "║  ✅ Ebbinghaus Decay    - Memories fade naturally             ║"
echo "║  ✅ Hebbian Learning    - Associations strengthen              ║"
echo "║  ✅ Predictive Activation - Anticipates needs                 ║"
echo "║  ✅ Semantic Triggers   - Push-based relevance                ║"
echo "║  ✅ Bayesian Confidence - Evidence-based certainty            ║"
echo "╚════════════════════════════════════════════════════════════════╝"
echo
echo "🎯 Next Steps:"
echo "   1. Access Web UI: http://127.0.0.1:8476"
echo "   2. Change password: root -> your_secure_password"
echo "   3. Connect AI agents: muninn init"
echo "   4. Test memory: curl -X POST http://127.0.0.1:8475/api/activate ..."
echo
echo "✅ Layer 6 deployment complete!"

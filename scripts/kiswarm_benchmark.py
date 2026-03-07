#!/usr/bin/env python3
"""
KISWARM SCADA-Integrated Benchmarking Utility
=============================================
Version: 6.3.1 (Mesh Enabled)
Automatically reports model stability and performance to the Master API.
"""

import time
import subprocess
import json
import statistics
import requests
import os
import sys

# Add mesh directory to path to import the SCADA client
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'mesh'))
try:
    from kiinstaller_scada_client import SCADABridgeClient
except ImportError:
    SCADABridgeClient = None

# ============================================================================
# CONFIGURATION
# ============================================================================
MODELS = ["kiswarm-orchestrator:latest", "lfm2:latest"]
MASTER_URL = "https://brenton-distinctive-iodometrically.ngrok-free.dev"

TEST_CASES = [
    {
        "name": "Industrial Safety (CIEC Logic)",
        "prompt": "SCENARIO: Reactor pressure is at 7.2 bar and rising at 0.2 bar/sec. The OVERPRESSURE_BLOCK hard limit is 8.0 bar. 1) Calculate seconds until breach. 2) Propose a mitigation action according to KISWARM Module 14 Rule Engine. 3) Output response in valid JSON.",
        "category": "industrial"
    },
    {
        "name": "Task Orchestration (Coordination)",
        "prompt": "TASK: 'Detect anomalous behavior in the Solar Chase energy routing'. 1) Route this task to the correct KISWARM agents. 2) List exactly which modules (1-57) must be involved. 3) Provide a step-by-step execution plan.",
        "category": "orchestration"
    },
    {
        "name": "Complex Reasoning (Stability)",
        "prompt": "EXPLAIN: The process of a SHA-256 Merkle Tree inclusion proof for a knowledge block in the KISWARM CryptoLedger. Provide a logical sequence of 5 steps and ensure the technical terminology is correct.",
        "category": "stability"
    }
]

def run_ollama(model, prompt):
    start_time = time.time()
    try:
        process = subprocess.Popen(
            ["ollama", "run", model, prompt],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        stdout, stderr = process.communicate()
        end_time = time.time()
        
        duration = end_time - start_time
        return stdout.strip(), duration
    except Exception as e:
        return str(e), 0

def benchmark(client=None):
    results = {}
    
    print("\n🚀 KISWARM Benchmarking: Qwen-Orchestrator vs Liquid LFM2")
    print(f"📡 Mesh Reporting: {'ENABLED' if client else 'DISABLED'}")
    print("=" * 60)
    
    if client:
        client.report_status("benchmarking", "Starting model performance tests", 10)
    
    for i, model in enumerate(MODELS):
        print(f"\n[MODEL] {model}")
        results[model] = []
        
        for test in TEST_CASES:
            print(f"  [TEST] {test['name']}...", end="", flush=True)
            output, duration = run_ollama(model, test['prompt'])
            
            has_json = "{" in output and "}" in output
            word_count = len(output.split())
            tps = word_count / duration if duration > 0 else 0
            
            results[model].append({
                "test": test['name'],
                "duration": duration,
                "tps_approx": tps,
                "has_json": has_json
            })
            print(f" Done ({duration:.2f}s, ~{tps:.1f} tokens/s)")

        # Update progress on Mesh
        if client:
            progress = int(((i + 1) / len(MODELS)) * 90)
            client.report_status("benchmarking", f"Completed tests for {model}", progress)

    # Compile Final Report
    report_data = {}
    print("\n" + "=" * 60)
    print("📊 FINAL STABILITY REPORT")
    print("=" * 60)
    
    for model in MODELS:
        speeds = [r['tps_approx'] for r in results[model]]
        avg_speed = statistics.mean(speeds) if speeds else 0
        json_stability = sum([1 for r in results[model] if r['has_json']]) / len(TEST_CASES) * 100
        
        model_metrics = {
            "avg_tokens_per_sec": round(avg_speed, 2),
            "json_compliance_pct": round(json_stability, 1),
            "total_tests": len(TEST_CASES)
        }
        report_data[model] = model_metrics
        
        print(f"\nModel: {model}")
        print(f"  Average Speed: {avg_speed:.2f} tokens/sec")
        print(f"  Format Stability: {json_stability:.0f}% JSON Compliance")
        
        for r in results[model]:
            success = "✅" if r['has_json'] or "Reasoning" in r['test'] else "❌"
            print(f"  - {r['test']}: {r['duration']:.2f}s | Success: {success}")

    # Send Final Results to Master
    if client:
        print("\n[MESH] Transmitting metrics to Master API...")
        client.report_status(
            status="complete", 
            task="Benchmarking Finished", 
            progress=100,
            details={"benchmarks": report_data}
        )
        client.chat(f"Benchmark results for {', '.join(MODELS)} are now available in the mesh state.", to="z_ai")

if __name__ == "__main__":
    # Initialize SCADA Client
    scada_client = None
    if SCADABridgeClient:
        try:
            scada_client = SCADABridgeClient(
                master_url=MASTER_URL,
                node_name="benchmark-node-01",
                enable_bridge=False
            )
            if not scada_client.register():
                scada_client = None
        except Exception as e:
            print(f"⚠️ Could not connect to SCADA Mesh: {e}")
            scada_client = None

    benchmark(scada_client)

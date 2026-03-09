#!/usr/bin/env python3
"""
KISWARM SCADA v6.3.0 - GitHub Mesh Router
========================================
Processes Mesh Commands stored as GitHub Issues.
Provides 24/7 redundancy for the KISWARM Mesh.
"""

import os
import json
import requests
import time
from datetime import datetime

# ============================================================================
# CONFIGURATION
# ============================================================================
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
REPO = "Baronki/KISWARMAGENTS1.0"
STATE_PATH = "docs/mesh_state.json"

class GitHubMeshRouter:
    def __init__(self):
        self.headers = {
            "Authorization": f"token {GITHUB_TOKEN}",
            "Accept": "application/vnd.github.v3+json"
        }
        self.base_url = f"https://api.github.com/repos/{REPO}"
        self.state = self._load_state()

    def _load_state(self):
        """Loads mesh state from repository if exists"""
        if os.path.exists(STATE_PATH):
            with open(STATE_PATH, 'r') as f:
                return json.load(f)
        return {"nodes": {}, "trust_scores": {}, "message_queue": [], "round_id": 0}

    def _save_state(self):
        """Saves current state to local file for GH Action to commit"""
        os.makedirs(os.path.dirname(STATE_PATH), exist_ok=True)
        with open(STATE_PATH, 'w') as f:
            json.dump(self.state, f, indent=2)

    def fetch_mesh_commands(self):
        """Fetches open issues with label 'mesh-command'"""
        url = f"{self.base_url}/issues?labels=mesh-command&state=open"
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        return []

    def process_command(self, issue):
        """Parses and executes command from issue body"""
        try:
            # Body expected to be JSON
            data = json.loads(issue['body'])
            command = data.get("command")
            entity_id = data.get("entity_id")
            
            print(f"[ROUTER] Processing {command} from {entity_id}")
            
            if command == "MESH_REGISTER":
                self.state["nodes"][entity_id] = {
                    "capabilities": data["payload"].get("capabilities", []),
                    "endpoint": data["payload"].get("endpoint"),
                    "last_seen": datetime.now().isoformat(),
                    "status": "active"
                }
                self.state["trust_scores"][entity_id] = 0.8 # Initial trust
                
            elif command == "MESH_HEARTBEAT":
                if entity_id in self.state["nodes"]:
                    self.state["nodes"][entity_id].update({
                        "last_seen": datetime.now().isoformat(),
                        "telemetry": data.get("payload", {})
                    })

            # Close the issue after processing
            self._close_issue(issue['number'], f"Command {command} processed successfully.")
            return True
        except Exception as e:
            self._close_issue(issue['number'], f"Error processing command: {str(e)}")
            return False

    def _close_issue(self, issue_number, comment):
        """Closes processed command issue"""
        # Post comment
        requests.post(f"{self.base_url}/issues/{issue_number}/comments", 
                      headers=self.headers, json={"body": comment})
        # Close issue
        requests.patch(f"{self.base_url}/issues/{issue_number}", 
                       headers=self.headers, json={"state": "closed"})

    def run(self):
        commands = self.fetch_mesh_commands()
        print(f"[ROUTER] Found {len(commands)} pending commands.")
        for cmd in commands:
            self.process_command(cmd)
        self._save_state()

if __name__ == "__main__":
    router = GitHubMeshRouter()
    router.run()

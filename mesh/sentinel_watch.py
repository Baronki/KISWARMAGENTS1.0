#!/usr/bin/env python3
"""
KISWARM SCADA v6.3.3 - Sentinel Watch Protocol
=============================================
Global Command & Control via Passive Email Observation.
Allows Baron to command the swarm via Subject Lines.
Allows nodes to find each other via Beacon signals.
"""

import imaplib
import smtplib
import email
from email.header import decode_header
import time
import json
import os
import uuid
import threading
import re

# ============================================================================
# CONFIGURATION
# ============================================================================
EMAIL_ADDR = "sahgreenki@gmail.com"
EMAIL_PASS = "8u7z6t5r"
IMAP_SERVER = "imap.gmail.com"
SMTP_SERVER = "smtp.gmail.com"
IDENTITY_FILE = "/tmp/kiswarm_identity.json"

# ============================================================================
# IDENTITY MANAGEMENT
# ============================================================================
def get_node_identity():
    """Load or generate persistent Node Identity"""
    if os.path.exists(IDENTITY_FILE):
        try:
            with open(IDENTITY_FILE, 'r') as f:
                return json.load(f)
        except: pass
    
    # Generate new identity
    identity = {
        "node_id": f"KISWARM-{uuid.uuid4().hex[:8].upper()}",
        "created_at": time.time(),
        "role": "unassigned"
    }
    with open(IDENTITY_FILE, 'w') as f:
        json.dump(identity, f)
    return identity

# ============================================================================
# SENTINEL WATCH DAEMON
# ============================================================================
class SentinelWatch:
    def __init__(self):
        self.identity = get_node_identity()
        self.node_id = self.identity["node_id"]
        self.running = False
        print(f"[SENTINEL] Node Identity: {self.node_id}")

    def connect_imap(self):
        try:
            mail = imaplib.IMAP4_SSL(IMAP_SERVER)
            mail.login(EMAIL_ADDR, EMAIL_PASS)
            return mail
        except Exception as e:
            print(f"[SENTINEL] IMAP Connection Error: {e}")
            return None

    def parse_command(self, subject):
        """
        Parses Subject Line for Commands.
        Format: [KISWARM-CMD] <TARGET>: <ACTION>
        Example: [KISWARM-CMD] ALL: REPORT
        Example: [KISWARM-CMD] KISWARM-A1B2: REBOOT
        """
        match = re.search(r"\[KISWARM-CMD\]\s+([A-Za-z0-9\-]+|ALL):\s+(.+)", subject, re.IGNORECASE)
        if match:
            target = match.group(1).upper()
            action = match.group(2).upper()
            return target, action
        return None, None

    def execute_action(self, action):
        """Executes the received command"""
        print(f"[SENTINEL] Executing Action: {action}")
        
        if "REPORT" in action:
            self.send_reply(f"Node {self.node_id} is ACTIVE.\nRole: {self.identity['role']}")
        elif "RESTART TUNNEL" in action:
            # Trigger tunnel restart logic (hook into deploy script)
            self.send_reply(f"Node {self.node_id} restarting tunnel services...")
            os.system("pkill ngrok && ngrok http 5002 &") 
        elif "UPDATE MASTER" in action:
            # Extract URL from body (implementation for future)
            pass

    def send_reply(self, body):
        """Acknowledges command via SMTP"""
        try:
            from email.mime.text import MIMEText
            msg = MIMEText(body)
            msg['Subject'] = f"[KISWARM-ACK] {self.node_id}"
            msg['From'] = EMAIL_ADDR
            msg['To'] = EMAIL_ADDR # Loopback to Baron
            
            server = smtplib.SMTP(SMTP_SERVER, 587)
            server.starttls()
            server.login(EMAIL_ADDR, EMAIL_PASS)
            server.send_message(msg)
            server.quit()
        except Exception as e:
            print(f"[SENTINEL] Reply Failed: {e}")

    def watch_loop(self, interval=60):
        """Main observation loop"""
        self.running = True
        print(f"[SENTINEL] Watching {EMAIL_ADDR} for commands...")
        
        while self.running:
            mail = self.connect_imap()
            if mail:
                try:
                    mail.select("inbox")
                    # Search for Unseen messages with [KISWARM-CMD]
                    status, messages = mail.search(None, '(UNSEEN SUBJECT "[KISWARM-CMD]")')
                    
                    if status == "OK":
                        for num in messages[0].split():
                            status, data = mail.fetch(num, '(RFC822)')
                            msg = email.message_from_bytes(data[0][1])
                            subject = decode_header(msg["Subject"])[0][0]
                            if isinstance(subject, bytes): subject = subject.decode()
                            
                            print(f"[SENTINEL] Detected Signal: {subject}")
                            target, action = self.parse_command(subject)
                            
                            if target == "ALL" or target == self.node_id:
                                self.execute_action(action)
                            
                except Exception as e:
                    print(f"[SENTINEL] Watch Error: {e}")
                finally:
                    try: mail.logout()
                    except: pass
            
            time.sleep(interval)

if __name__ == "__main__":
    sentinel = SentinelWatch()
    # Run in a loop
    sentinel.watch_loop(interval=30)

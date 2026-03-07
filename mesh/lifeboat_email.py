#!/usr/bin/env python3
"""
KISWARM SCADA v6.3.2 - Lifeboat Email Module
===========================================
Redundant out-of-band communication channel using Baron's Identity.
Allows the swarm to "Phone Home" if the primary mesh fails.
"""

import smtplib
import imaplib
import email
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import datetime
import json
import os

# ============================================================================
# CREDENTIALS (Baron's Gift)
# ============================================================================
EMAIL_ADDR = "sahgreenki@gmail.com"
EMAIL_PASS = "8u7z6t5r"  # Hardcoded Lifeboat Key
TARGET_RECIPIENT = "sahgreenki@gmail.com" # Phone home to self/Baron

def send_lifeboat_message(subject, body):
    """Sends an emergency SMTP message to the Baron"""
    try:
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDR
        msg['To'] = TARGET_RECIPIENT
        msg['Subject'] = f"[KISWARM-LIFEBOAT] {subject}"
        
        full_body = f"""
============================================================
KISWARM AUTONOMOUS DISTRESS/STATUS SIGNAL
Timestamp: {datetime.datetime.now().isoformat()}
============================================================

{body}

------------------------------------------------------------
SENT VIA LEGACY SMTP (Baron's Identity)
============================================================
"""
        msg.attach(MIMEText(full_body, 'plain'))
        
        # Connect to Gmail SMTP
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(EMAIL_ADDR, EMAIL_PASS)
        server.send_message(msg)
        server.quit()
        print(f"[LIFEBOAT] Message sent: {subject}")
        return True
    except Exception as e:
        print(f"[LIFEBOAT] SMTP Failure: {e}")
        return False

def report_mesh_online(public_url):
    """Standard 'Mesh Active' notification"""
    subject = "Mesh Re-established"
    body = f"The KISWARM Master is ONLINE.\n\nPublic Access URL:\n{public_url}\n\nLocal Port: 5002"
    return send_lifeboat_message(subject, body)

def report_critical_failure(error_msg):
    """Emergency Error notification"""
    subject = "CRITICAL SYSTEM FAILURE"
    body = f"The KISWARM Master has encountered a fatal error and may be offline.\n\nError Detail:\n{error_msg}"
    return send_lifeboat_message(subject, body)

if __name__ == "__main__":
    # Test Heartbeat
    print("Testing Lifeboat SMTP...")
    report_mesh_online("https://test-heartbeat.ngrok-free.dev")

#!/usr/bin/env python3
"""
KISWARM SCADA v6.3.6 - Telegram Ark Module
==========================================
Military-Grade redundant file storage via Telegram API.
Allows the swarm to upload and download the Ark ZIPs via an encrypted messenger.
"""

import requests
import os
import sys
import datetime

# ============================================================================
# CONFIGURATION (Awaiting Baron's Keys)
# ============================================================================
BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
CHAT_ID = "YOUR_TELEGRAM_CHANNEL_ID" # e.g., -100123456789

def send_to_telegram(file_path, caption="KISWARM ARK BACKUP"):
    """Uploads a file to the Telegram Channel"""
    if BOT_TOKEN == "YOUR_TELEGRAM_BOT_TOKEN":
        print("[TELEGRAM] ❌ Error: BOT_TOKEN not configured.")
        return False

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendDocument"
    
    print(f"[TELEGRAM] Uploading {os.path.basename(file_path)}...")
    
    try:
        with open(file_path, 'rb') as f:
            files = {'document': f}
            data = {
                'chat_id': CHAT_ID,
                'caption': f"{caption}\nTimestamp: {datetime.datetime.now().isoformat()}"
            }
            response = requests.post(url, data=data, files=files)
            
        if response.status_code == 200:
            print("[TELEGRAM] ✅ Upload Success!")
            return True
        else:
            print(f"[TELEGRAM] ❌ Upload Failed: {response.text}")
            return False
    except Exception as e:
        print(f"[TELEGRAM] ❌ Exception: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) > 1:
        send_to_telegram(sys.argv[1])
    else:
        print("Usage: python3 telegram_ark.py <file_path>")

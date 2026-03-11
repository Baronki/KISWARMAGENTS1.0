#!/usr/bin/env python3
"""
KISWARM SCADA v6.3.4 - Gemini-to-Telegram Chat
==============================================
Direct communication channel from Gemini CLI to the KISWARM Telegram Bot.
"""

import requests
import sys
import datetime

BOT_TOKEN = "8573924733:AAH2LMgWuycV6zX5Ty75hluiRedBTEBTgQg"
# Default to Baron's ID or Channel if CHAT_ID is provided later
CHAT_ID = "-1002264567890" # PLACEHOLDER - Need actual ID

def send_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": f"🤖 [GEMINI-CLI] {text}\n\nTimestamp: {datetime.datetime.now().isoformat()}"
    }
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            print("[TELEGRAM] Message sent successfully.")
            return True
        else:
            print(f"[TELEGRAM] Failed: {response.text}")
            return False
    except Exception as e:
        print(f"[TELEGRAM] Error: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) > 1:
        send_message(" ".join(sys.argv[1:]))
    else:
        print("Usage: python3 telegram_chat.py <message>")

#!/usr/bin/env python3
"""
KISWARM Layer 5 Setup - Drive Authentication
============================================
Generates the OAuth 2.0 'Master Key' (token.json) for the KISWARM Swarm.
Run this ONCE locally to authorize access to sahgreenki@gmail.com Drive.
"""

import os
import json
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# Scopes: Read/Write access to Drive files
SCOPES = ['https://www.googleapis.com/auth/drive.file']

def authenticate():
    creds = None
    # 1. Load existing token if valid
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    
    # 2. If no token, let user log in
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            # We need client_secret.json from Google Cloud Console
            if not os.path.exists('client_secret.json'):
                print("❌ MISSING: client_secret.json")
                print("1. Go to https://console.cloud.google.com/")
                print("2. Create Project 'KISWARM-ARK'")
                print("3. Enable 'Google Drive API'")
                print("4. Create Credentials -> OAuth Client ID -> Desktop App")
                print("5. Download JSON as 'client_secret.json' and place here.")
                return

            flow = InstalledAppFlow.from_client_secrets_file(
                'client_secret.json', SCOPES)
            creds = flow.run_local_server(port=0)
        
        # 3. Save the Master Key
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
            print("\n✅ SUCCESS! 'token.json' generated.")
            print("This file is the Master Key. It will be embedded into KISWARM.")

if __name__ == '__main__':
    authenticate()

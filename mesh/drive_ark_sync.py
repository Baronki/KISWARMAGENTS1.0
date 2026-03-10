#!/usr/bin/env python3
"""
KISWARM Layer 5 - Drive Ark Sync Engine
=======================================
Autonomously archives the KISWARM source code to Google Drive.
Updates versions.json to point to the latest "Deep Archive" build.
"""

import os
import json
import shutil
import hashlib
from datetime import datetime
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

# ============================================================================
# CONFIGURATION
# ============================================================================
TOKEN_PATH = os.path.join(os.path.dirname(__file__), 'token.json')
REPO_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
ARCHIVE_NAME = "KISWARM_SOURCE"
DRIVE_FOLDER_NAME = "KISWARM_ARK"

class DriveArkSync:
    def __init__(self):
        if not os.path.exists(TOKEN_PATH):
            raise FileNotFoundError("Missing token.json! Run setup_drive_auth.py first.")
        
        creds = Credentials.from_authorized_user_file(TOKEN_PATH)
        self.service = build('drive', 'v3', credentials=creds)

    def _get_folder_id(self, folder_name):
        """Finds or creates the KISWARM_ARK folder"""
        query = f"name='{folder_name}' and mimeType='application/vnd.google-apps.folder' and trashed=false"
        results = self.service.files().list(q=query, fields="files(id)").execute()
        files = results.get('files', [])
        
        if files:
            return files[0]['id']
        else:
            file_metadata = {
                'name': folder_name,
                'mimeType': 'application/vnd.google-apps.folder'
            }
            file = self.service.files().create(body=file_metadata, fields='id').execute()
            print(f"[DRIVE] Created Ark Folder: {file.get('id')}")
            return file.get('id')

    def create_archive(self):
        """Zips the repository"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{ARCHIVE_NAME}_{timestamp}"
        output_path = os.path.join("/tmp", filename)
        
        print(f"[LOCAL] Zipping {REPO_PATH}...")
        shutil.make_archive(output_path, 'zip', REPO_PATH)
        
        zip_path = output_path + ".zip"
        
        # Calculate SHA256
        sha256_hash = hashlib.sha256()
        with open(zip_path, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        
        return zip_path, filename + ".zip", sha256_hash.hexdigest()

    def upload_archive(self, file_path, file_name, folder_id):
        """Uploads zip to Drive"""
        file_metadata = {
            'name': file_name,
            'parents': [folder_id]
        }
        media = MediaFileUpload(file_path, mimetype='application/zip', resumable=True)
        
        print(f"[DRIVE] Uploading {file_name}...")
        file = self.service.files().create(
            body=file_metadata,
            media_body=media,
            fields='id'
        ).execute()
        
        print(f"[DRIVE] Upload Complete. File ID: {file.get('id')}")
        return file.get('id')

    def update_manifest(self, folder_id, file_id, file_name, file_hash):
        """Updates versions.json on Drive"""
        manifest_name = "versions.json"
        
        # 1. Check for existing manifest
        query = f"name='{manifest_name}' and '{folder_id}' in parents and trashed=false"
        results = self.service.files().list(q=query, fields="files(id)").execute()
        files = results.get('files', [])
        
        # 2. Build new manifest data
        manifest_data = {
            "latest": {
                "version": file_name,
                "file_id": file_id,
                "sha256": file_hash,
                "updated_at": datetime.now().isoformat()
            },
            "history": [] # TODO: Append history
        }
        
        # 3. Save locally
        local_manifest = "/tmp/versions.json"
        with open(local_manifest, 'w') as f:
            json.dump(manifest_data, f, indent=2)
            
        # 4. Upload/Update
        media = MediaFileUpload(local_manifest, mimetype='application/json')
        
        if files:
            # Update existing
            self.service.files().update(
                fileId=files[0]['id'],
                media_body=media
            ).execute()
            print("[DRIVE] Manifest Updated.")
        else:
            # Create new
            file_metadata = {
                'name': manifest_name,
                'parents': [folder_id]
            }
            self.service.files().create(
                body=file_metadata,
                media_body=media,
                fields='id'
            ).execute()
            print("[DRIVE] Manifest Created.")

    def run(self):
        print("="*60)
        print("KISWARM Layer 5 Sync Engine")
        print("="*60)
        
        folder_id = self._get_folder_id(DRIVE_FOLDER_NAME)
        zip_path, zip_name, zip_hash = self.create_archive()
        file_id = self.upload_archive(zip_path, zip_name, folder_id)
        self.update_manifest(folder_id, file_id, zip_name, zip_hash)
        
        # Cleanup
        os.remove(zip_path)
        print("\n✅ Layer 5 Sync Complete.")

if __name__ == "__main__":
    try:
        syncer = DriveArkSync()
        syncer.run()
    except Exception as e:
        print(f"❌ Sync Failed: {e}")

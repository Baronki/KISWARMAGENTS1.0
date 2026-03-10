# KISWARM Layer 5: Google Drive Ark Protocol (Deep Storage)

## 1. Concept
A "Shadow Repository" hosted on the `sahgreenki@gmail.com` Google Drive. It provides a censorship-resistant, high-availability fallback for source code and model weights.

## 2. Storage Structure
```text
Google Drive Root
└── KISWARM_ARK/
    ├── versions.json          # The "Git Log" (Latest version pointer)
    ├── source/
    │   ├── KISWARM_v6.3.0.zip # Source Code Archives
    │   └── KISWARM_v6.3.4.zip
    └── models/
        ├── orchestrator.gguf  # Model Weights (Future 100GB Expansion)
        └── lfm2.gguf
```

## 3. Workflow
1.  **Master Node** runs `drive_sync.py` every hour.
2.  It zips local `KISWARMAGENTS1.0`, calculates SHA256 hash.
3.  Uploads to `KISWARM_ARK/source/`.
4.  Updates `versions.json` with the new link.

## 4. Fallback Logic (KIInstaller)
```python
try:
    git_clone("github.com/Baronki/KISWARM...")
except GitError:
    print("⚠️ GitHub Blocked. Engaging Layer 5...")
    drive = GoogleDriveArk(token=EMBEDDED_TOKEN)
    drive.download_latest_source()
```

## 5. Security
The `token.json` (OAuth Refresh Token) is encrypted and embedded in the installer. It grants "File Editor" access only to the KISWARM folder, protecting the rest of the account.

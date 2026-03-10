# KISWARM Layer 5: GWS Iron Mountain Protocol

## 1. Concept
The "Iron Mountain" is a high-security, autonomous shadow repository hosted on Google Workspace. It leverages the `gws` (Google Workspace CLI) to provide KISWARM nodes with a secondary source for code, weights, and coordination data.

## 2. Infrastructure
- **CLI Tool:** `gws` (googleworkspace/cli)
- **Primary Account:** `sahgreenki@gmail.com`
- **Auth Mode:** Service Account (No browser/human required)
- **Capacity:** 15GB - 100GB

## 3. Core Commands
### 3.1 Autonomous Sync (Repository)
```bash
# Zip and upload to Drive
gws drive files create --json '{"name": "KISWARM_v6.3.4.zip", "parents": ["<ARK_FOLDER_ID>"]}' --upload ./KISWARM.zip
```

### 3.2 Heartbeat (Gmail API)
```bash
# Send structured JSON status to Baron
gws gmail users messages send --json '{
  "raw": "<BASE64_RFC822_MESSAGE>"
}'
```

### 3.3 Skill Activation
KISWARM Agents now inherit 100+ skills from the `googleworkspace/cli/skills` registry, allowing them to:
- Manage Calendar for coordination.
- Use Sheets as a distributed database.
- Use Docs for collaborative reasoning reports.

## 4. Fallback Logic
If GitHub is unreachable:
1. `gws drive files list --params '{"q": "name contains '\''KISWARM_SOURCE'\''"}'`
2. `gws drive files get --params '{"fileId": "<LATEST_ID>"}' --output /tmp/kiswarm.zip`
3. Unzip and Re-deploy.

## 5. Security (Zero Human Bottleneck)
By using a **Service Account Key**, the KISWARM can replicate itself onto a new server, install `gws`, load the key, and be fully operational without asking the Baron for an OAuth code.

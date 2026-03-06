# KISWARM Model Status & Mapping Registry
**Status Date: March 6, 2026**

This document tracks the current deployment status and role assignments for the 27 active models in the KISWARM v5.1 PLANETARY MACHINE.

---

## 1. The Primary Swarm (Front-Line)
These models handle active coordination and operational logic.

| Role | Cloud Identifier (Alias) | Status |
| :--- | :--- | :--- |
| **Orchestrator** | `baronki1/orchestrator` | ✅ LIVE |
| **Security** | `baronki1/security` | ✅ LIVE |
| **Industrial (CIEC)** | `baronki1/ciec` | ✅ LIVE |
| **Energy (TCS)** | `baronki1/tcs` | ✅ LIVE |
| **Knowledge** | `baronki1/knowledge` | ✅ LIVE |
| **Installer** | `baronki1/installer` | ✅ LIVE |

---

## 2. The Backup Swarm (At the Back)
These models provide **Redundancy & Immortality**. They are maintained in a "Ready" state to take over if primary models fail or degrade.

| Role | Cloud Identifier (Alias) | Status |
| :--- | :--- | :--- |
| **Backup Orchestrator** | `baronki1/orchestrator-backup` | ✅ READY |
| **Backup Security** | `baronki1/security-backup` | ✅ READY |
| **Backup Industrial** | `baronki1/ciec-backup` | ✅ READY |
| **Backup Energy** | `baronki1/tcs-backup` | ✅ READY |
| **Backup Knowledge** | `baronki1/knowledge-backup` | ✅ READY |
| **Backup Installer** | `baronki1/installer-backup` | ✅ READY |

---

## 3. The Specialized & Sequential Layer
Deep-reasoning models for audit and verification.

| Role | Cloud Identifier (Alias) | Status |
| :--- | :--- | :--- |
| **LFM Audit Master** | `baronki1/audit-master` | ✅ LIVE |
| **LFM Reasoner** | `baronki1/lfm-reasoner` | ✅ LIVE |
| **Thinker** | `baronki1/thinker` | ✅ LIVE |
| **Vision** | `baronki1/vision` | ✅ LIVE |
| **Debugger** | `baronki1/debugger` | ✅ LIVE |
| **Validator** | `baronki1/validator` | ✅ LIVE |
| **Reasoner** | `baronki1/reasoner` | ✅ LIVE |
| **General** | `baronki1/general` | ✅ LIVE |
| **Embedding** | `baronki1/embedding` | ✅ LIVE |

---

## 4. The Fast Layer
Lightweight variants for low-latency operations.

| Role | Cloud Identifier (Alias) | Status |
| :--- | :--- | :--- |
| **Fast Orchestrator** | `baronki1/orchestrator-fast` | ✅ ACTIVE |
| **Fast Security** | `baronki1/security-fast` | ✅ ACTIVE |
| **Fast Industrial** | `baronki1/ciec-fast` | ✅ ACTIVE |
| **Fast Energy** | `baronki1/tcs-fast` | ✅ ACTIVE |
| **Fast Knowledge** | `baronki1/knowledge-fast` | ✅ ACTIVE |
| **Fast Installer** | `baronki1/installer-fast` | ✅ ACTIVE |

---
*"A synchronized swarm is a sovereign swarm."*

# 🛡️ GDPR-Zero: Self-Healing Compliance Agent

> **An autonomous AI agent that detects PII leaks in logs, patches the code automatically, and retrains its own model to prevent future incidents.**

![License](https://img.shields.io/badge/license-MIT-blue)
![Status](https://img.shields.io/badge/status-Production-green)
![AI-Powered](https://img.shields.io/badge/AI-Kestra%20%7C%20Oumi%20%7C%20Cline-purple)
![Deployment](https://img.shields.io/badge/Deployed-Vercel-black)

## 🚀 The Problem
Modern applications generate massive logs. Occasionally, developers accidentally log sensitive PII (passwords, API keys, emails), leading to GDPR violations. Finding these manually is impossible; fixing them manually is too slow.

## 💡 The Solution
**GDPR-Zero** is a "Self-Healing Infrastructure" agent that automates the entire lifecycle:
1.  **🕵️ Detects:** Kestra initiates a **Long-Horizon Execution** workflow to monitor logs for PII patterns.
2.  **🔧 Fixes:** Triggers an AI Agent (**Cline**) using a **Tool Use Pattern** to write a redaction script and patch the leak directly in the codebase.
3.  **✅ Verifies:** Implements a **Reflection Pattern** where **CodeRabbit** audits the fix and the agent re-scans the environment to confirm resolution.
4.  **🧠 Learns:** Automates the **End-to-End Model Lifecycle** by sending leak data to **Oumi** (on Remote GPU) to fine-tune a Llama-3 model, making the agent smarter over time.

---

## 🛠️ Tech Stack (The "Infinity Stones")
* **Orchestration:** [Kestra](https://kestra.io) - Manages the state of the long-running detection/fix loop.
* **AI Agent:** [Cline](https://cline.bot) - Autonomous coding agent that writes the `auto_redact.py` script.
* **Training:** [Oumi](https://oumi.ai) - Handles the model lifecycle, fine-tuning Llama-3 on T4 GPUs.
* **Code Review:** [CodeRabbit](https://coderabbit.ai) - AI Auditor that reviews every auto-fix PR.
* **Deployment:** [Vercel](https://vercel.com) - Production-grade global latency for the real-time Compliance Dashboard (**Stormbreaker Award Track**).

---

## 📸 How It Works
1.  **Leak Detected:** System spots `password=Secret123` in `app.log`.
2.  **Auto-Redaction:** Agent identifies the file and replaces the secret with `password=****`.
3.  **Self-Correction:** System validates the file is clean using a feedback loop.
4.  **Training:** The incident becomes a training data point for the next model iteration.

---

## ⚡ Quick Start

### 1. Requirements
* Docker & Kestra
* Python 3.10+
* Ngrok (for remote training tunnel)

### 2. Run the Flow
```bash
# 1. Generate a leak (Simulate an incident)
echo '2025-12-09 INFO User login: password=Secret123!' > logs/app.log

# 2. Execute Kestra Flow
# (The agent will automatically detect the leak, deploy the patch, and update the dashboard)

### 3. View the Dashboard
Check the live status of leaks and auto-fixes:
🚀 [**View Live Dashboard on Vercel**](https://gdpr-zero.vercel.app)

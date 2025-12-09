# 🛡️ GDPR-Zero: Self-Healing Compliance Agent

> **An autonomous AI agent that detects PII leaks in logs, patches the code automatically, and retrains its own model to prevent future incidents.**

![License](https://img.shields.io/badge/license-MIT-blue)
![Status](https://img.shields.io/badge/status-Production-green)
![AI-Powered](https://img.shields.io/badge/AI-Kestra%20%7C%20Oumi%20%7C%20Cline-purple)

## 🚀 The Problem
Modern applications generate massive logs. Occasionally, developers accidentally log sensitive PII (passwords, API keys, emails), leading to GDPR violations. finding these manually is impossible.

## 💡 The Solution
**GDPR-Zero** is an autonomous loop that:
1.  **🕵️ Detects:** Kestra watches logs for PII patterns (RegEx + AI).
2.  **🔧 Fixes:** Triggers an AI Agent (**Cline**) to write a redaction script and patch the leak.
3.  **🧠 Learns:** Sends the leak data to **Oumi** (on Remote GPU) to fine-tune a Llama-3 model.
4.  **✅ Verifies:** **CodeRabbit** audits the fix, and the Dashboard updates to Green.

---

## 🛠️ Tech Stack (The "Infinity Stones")
* **Orchestration:** [Kestra](https://kestra.io) (Manages the detection/fix loop)
* **AI Agent:** [Cline](https://cline.bot) (Writes the `auto_redact.py` script)
* **Training:** [Oumi](https://oumi.ai) (Fine-tunes Llama-3 on Colab T4 GPU)
* **Code Review:** [CodeRabbit](https://coderabbit.ai) (Reviews every auto-fix PR)
* **Deployment:** [Vercel](https://vercel.com) (Hosts the Compliance Dashboard)

---

## 📸 How It Works
1.  **Leak Detected:** System spots `password=Secret123` in `app.log`.
2.  **Auto-Redaction:** Python script replaces it with `password=****`.
3.  **Self-Correction:** System validates the file is clean.
4.  **Training:** Model retrains to recognize this context in the future.

---

## ⚡ Quick Start

### 1. Requirements
* Docker & Kestra
* Python 3.10+
* Ngrok (for remote training)

### 2. Run the Flow
```bash
# 1. Generate a leak
echo '2025-12-09 INFO User login: password=Secret123!' > logs/app.log

# 2. Execute Kestra Flow
# (The agent will automatically detect, fix, and resolve the issue)

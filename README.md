# Awesome OpenClaw Automations 🚀

<img width="1376" height="768" alt="image" src="https://github.com/user-attachments/assets/935628b6-0b03-42a5-bbc7-895329473c74" />

A curated collection of production-grade automation recipes, custom system prompts, and scheduled workflows for [OpenClaw](https://github.com), the local-first open-source AI assistant.

These automations enable your OpenClaw agent to manage your inbox, scrape web data, monitor pull requests, and deliver reports directly to your preferred chat channels (WhatsApp, Telegram, Discord).

## 📂 Repository Structure
* `/system-prompts`: Core personalities and strict execution guardrails.
* `/cron-jobs`: Scheduled background tasks and data pipeline scripts.
* `/workflows`: End-to-end multi-step task configurations.

---

## 🛠️ Ready-to-Use Automations

### 1. Zero Inbox & Urgent Lead Alerter
* **Folder:** `workflows/inbox-zero/`
* **Description:** Periodically monitors your Gmail workspace, auto-summarizes unread threads, and instantly highlights urgent leads or system failures to your Telegram/WhatsApp chat.

### 2. Autonomous Hacker News AI Monitor
* **Folder:** `cron-jobs/hn-monitor/`
* **Description:** Background worker that polls Hacker News API, filters items using target ML/AI keywords, and compiles a clean daily digest message.

### 3. Automated GitHub Code Reviewer & PR Summarizer
* **Folder:** `workflows/github-reviewer/`
* **Description:** Listens to incoming Pull Requests, uses OpenClaw’s native code capabilities to spot syntax/security vulnerabilities, and leaves a markdown comment with optimization tips.

---

## 🚀 How to Setup

1. **Clone this repository:**
   ```bash
   git clone https://github.com
   ```
2. Copy the desired automation folder or `.env` parameters into your local OpenClaw gateway deployment directory.
3. Ensure your target API keys (`OPENAI_API_KEY` or `ANTHROPIC_API_KEY`) and platform tokens (`TELEGRAM_BOT_TOKEN`, `GITHUB_TOKEN`) are properly configured.
4. Restart your node:
   ```bash
   openclaw update --channel stable
   ```

## 🤝 Contributing
Feel free to fork this repository, add your custom automated skills, and open a Pull Request!

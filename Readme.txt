# 🛡️ AI System Health Guardian

> An intelligent system monitoring agent that **observes** computer performance, **detects** unhealthy conditions, and **alerts** the user automatically — built using Python and the Observe-Think-Act agentic loop.

---

## 🌍 Real-World Problem

Modern computers often slow down silently. Users don't notice high CPU usage, low memory, or overloaded processes — until it's too late and the system crashes or lags badly.

**AI System Health Guardian** solves this by acting as a 24/7 autonomous watchdog for your machine.

---

## 🤖 How It Works

The agent follows a continuous **Observe → Think → Act** loop:

| Stage | What it does |
|-------|-------------|
| **Observe** | Collects real-time CPU, RAM, and Disk metrics using `psutil` |
| **Think** | Applies rule-based logic to detect anomalies against thresholds |
| **Act** | Displays alerts in terminal + saves logs to `health_log.txt` |

---

## ✨ Features

- 📊 **Live terminal dashboard** with color-coded usage bars
- 🔴 **Critical alerts** when thresholds are exceeded
- 🟡 **Early warnings** when usage approaches dangerous levels
- 📋 **Top processes** display — see what's eating your CPU
- 📁 **Automatic log saving** to `health_log.txt` for analysis
- ⚙️ **Configurable thresholds** — easily adjust limits at the top of the file

---



## 📁 Project Structure

```
ai-system-health-guardian/
│
├── health_guardian.py   # Main agent code
├── health_log.txt       # Auto-generated alert log
└── README.md            # This file
```

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3 | Core language |
| `psutil` | System metrics collection |
| `os` / `time` | System interaction & timing |

---

## 🗺️ System Architecture

The agent follows the classic AI agentic loop:

```
┌─────────────────────────────────────┐
│        CONTINUOUS AGENTIC LOOP      │
│                                     │
│  [OBSERVE] ──► [THINK] ──► [ACT]   │
│      ▲                      │       │
│      └──────────────────────┘       │
└─────────────────────────────────────┘

OBSERVE  →  psutil reads CPU, RAM, Disk
THINK    →  Rule engine checks thresholds
ACT      →  Terminal alert + Log file saved
```

---

## 🔮 Future Improvements

- [ ] Desktop pop-up notifications (`plyer`)
- [ ] Auto-kill runaway processes
- [ ] Web-based dashboard (Flask)
- [ ] Email/SMS alerts
- [ ] ML-based anomaly detection (beyond fixed thresholds)

---

## 📌 Built With Help From

This project was built by Samir Adhikari, as part of a university AI course project.

---

## 📄 License

MIT License — free to use and modify.

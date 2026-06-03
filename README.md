# AI System Health Guardian

AI System Health Guardian is a Python-based intelligent monitoring agent that observes computer performance, detects unhealthy system conditions, alerts the user, and saves logs for later analysis.

## Real-World Problem

Modern computers can become slow because users often do not notice high CPU usage, high RAM usage, high disk usage, or too many heavy background processes until the system performance becomes poor. This project helps users identify these problems early.

## Project Goal

The goal of this project is to demonstrate an AI-style agent that follows the Observe → Think → Act loop:

- **Observe:** Monitor CPU, RAM, disk usage, and running processes.
- **Think:** Compare system values with predefined threshold rules.
- **Act:** Alert the user, suggest actions, and save logs.

## Features

- Monitors CPU usage
- Monitors RAM usage
- Monitors disk usage
- Detects unhealthy system conditions
- Shows warning messages in the terminal
- Shows top memory-consuming processes
- Saves text logs in `system_health_log.txt`
- Saves structured reports in `system_health_report.csv`
- Beginner-friendly Python code

## Technologies Used

- Python
- psutil
- time
- os
- csv
- datetime

## Installation

Install the required library:

```bash
pip install psutil
```

On Mac, if needed:

```bash
pip3 install psutil
```

## How to Run

Run the project with:

```bash
python ai_system_health_guardian.py
```

On Mac, if needed:

```bash
python3 ai_system_health_guardian.py
```

To stop the program, press:

```bash
CTRL + C
```

## Threshold Rules

The system uses these default rules:

- CPU usage ≥ 80% → Warning
- RAM usage ≥ 80% → Warning
- Disk usage ≥ 90% → Warning

## Output Files

After running the program, these files will be created automatically:

- `system_health_log.txt`
- `system_health_report.csv`

## System Diagram

The system follows this flow:

```text
Computer System
      ↓
Observe Module
CPU, RAM, Disk Monitoring
      ↓
Think Module
Rule-Based Decision Engine
      ↓
Act Module
Alert User + Save Logs + Suggest Actions
      ↓
Continuous Feedback Loop
```

## Demo Video Explanation Script

Hello everyone, my project is called AI System Health Guardian. This is an intelligent system monitoring agent built using Python.

The real-world problem is that many computer users do not notice high CPU usage, high RAM usage, or high disk usage until their computer becomes slow. My project solves this problem by continuously monitoring the system and alerting the user when something abnormal happens.

This project follows the Observe, Think, and Act agent loop. In the Observe stage, the system collects CPU, RAM, and disk usage using the psutil library. In the Think stage, it checks these values with threshold rules. For example, if CPU usage is more than 80 percent, the system marks it as a warning. In the Act stage, the system displays warning messages, suggests actions, shows top memory-consuming processes, and saves logs.

Now I will run the project. As you can see, the terminal shows current CPU, RAM, and disk usage. If everything is normal, it shows the system is healthy. If there is high usage, it gives a warning and suggests what the user should do.

This project is useful because it improves user awareness, helps detect system problems early, and supports better computer performance.

## LinkedIn Post

I am excited to share my project: AI System Health Guardian.

This is a Python-based intelligent monitoring agent that observes computer performance, detects unhealthy system conditions, and alerts the user automatically.

The project solves a real-world problem where computers become slow because users do not notice high CPU usage, high RAM usage, high disk usage, or heavy background processes early. My system continuously monitors CPU, RAM, and disk usage, applies rule-based decision logic, shows alerts, suggests actions, and saves logs for analysis.

The agent follows an Observe → Think → Act loop:

- Observe: Monitor CPU, RAM, disk usage, and processes
- Think: Detect unhealthy conditions using threshold rules
- Act: Alert the user, suggest actions, and save logs

Technologies used: Python, psutil, csv, datetime

GitHub Link: Add your GitHub repository link here

#Python #AI #AIAgent #SystemMonitoring #ComputerScience #StudentProject #GitHub

## Author

Arbin Bhattarai

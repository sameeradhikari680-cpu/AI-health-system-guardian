"""
AI System Health Guardian
=========================
An intelligent monitoring agent that observes system performance,
detects unhealthy conditions, and alerts the user automatically.

Author: [Your Name]
GitHub: [Your GitHub Link]
"""

import psutil
import time
import os
from datetime import datetime

# ─────────────────────────────────────────────
#  CONFIGURATION — tweak thresholds here
# ─────────────────────────────────────────────
CPU_THRESHOLD    = 85   # %
RAM_THRESHOLD    = 90   # %
DISK_THRESHOLD   = 95   # %
CHECK_INTERVAL   = 5    # seconds between checks
LOG_FILE         = "health_log.txt"

# ─────────────────────────────────────────────
#  ANSI COLORS for terminal output
# ─────────────────────────────────────────────
RED    = "\033[91m"
YELLOW = "\033[93m"
GREEN  = "\033[92m"
CYAN   = "\033[96m"
BOLD   = "\033[1m"
RESET  = "\033[0m"

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

# ─────────────────────────────────────────────
#  MODULE 1 — OBSERVE: collect system metrics
# ─────────────────────────────────────────────
def observe():
    """Collect current system health metrics."""
    cpu  = psutil.cpu_percent(interval=1)
    ram  = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent

    # Top 3 CPU-hungry processes
    processes = []
    for proc in sorted(
        psutil.process_iter(["pid", "name", "cpu_percent"]),
        key=lambda p: p.info["cpu_percent"] or 0,
        reverse=True
    )[:3]:
        processes.append(proc.info)

    return {
        "cpu":       cpu,
        "ram":       ram,
        "disk":      disk,
        "processes": processes,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }

# ─────────────────────────────────────────────
#  MODULE 2 — THINK: evaluate health rules
# ─────────────────────────────────────────────
def think(metrics):
    """Apply rule-based decision logic to detect anomalies."""
    alerts = []

    if metrics["cpu"] > CPU_THRESHOLD:
        alerts.append({
            "level":   "CRITICAL",
            "resource":"CPU",
            "value":   metrics["cpu"],
            "message": f"CPU usage is critically high at {metrics['cpu']}%! System may be overloaded.",
        })

    if metrics["ram"] > RAM_THRESHOLD:
        alerts.append({
            "level":   "CRITICAL",
            "resource":"RAM",
            "value":   metrics["ram"],
            "message": f"RAM usage is critically high at {metrics['ram']}%! Close unused applications.",
        })

    if metrics["disk"] > DISK_THRESHOLD:
        alerts.append({
            "level":   "CRITICAL",
            "resource":"DISK",
            "value":   metrics["disk"],
            "message": f"Disk usage is critically high at {metrics['disk']}%! Free up storage space.",
        })

    # Moderate warnings (within 10% of threshold)
    if CPU_THRESHOLD - 10 < metrics["cpu"] <= CPU_THRESHOLD:
        alerts.append({
            "level":   "WARNING",
            "resource":"CPU",
            "value":   metrics["cpu"],
            "message": f"CPU usage is elevated at {metrics['cpu']}%. Monitor closely.",
        })

    if RAM_THRESHOLD - 10 < metrics["ram"] <= RAM_THRESHOLD:
        alerts.append({
            "level":   "WARNING",
            "resource":"RAM",
            "value":   metrics["ram"],
            "message": f"RAM usage is elevated at {metrics['ram']}%. Consider closing tabs or apps.",
        })

    return alerts

# ─────────────────────────────────────────────
#  MODULE 3 — ACT: display alerts & save logs
# ─────────────────────────────────────────────
def act(metrics, alerts):
    """Display dashboard and save logs if anomalies detected."""
    clear_screen()

    # ── Header ──────────────────────────────
    print(f"{BOLD}{CYAN}")
    print("╔══════════════════════════════════════════════╗")
    print("║        AI SYSTEM HEALTH GUARDIAN  🛡️          ║")
    print("╚══════════════════════════════════════════════╝")
    print(f"{RESET}")
    print(f"  🕐 {metrics['timestamp']}\n")

    # ── Metrics ──────────────────────────────
    def bar(value, threshold):
        filled = int(value / 5)
        color = RED if value > threshold else (YELLOW if value > threshold - 10 else GREEN)
        return f"{color}{'█' * filled}{'░' * (20 - filled)}{RESET} {value:.1f}%"

    print(f"  {'CPU ':.<12} {bar(metrics['cpu'],  CPU_THRESHOLD)}")
    print(f"  {'RAM ':.<12} {bar(metrics['ram'],  RAM_THRESHOLD)}")
    print(f"  {'DISK ':.<12} {bar(metrics['disk'], DISK_THRESHOLD)}")

    # ── Top Processes ─────────────────────────
    print(f"\n  {BOLD}Top Processes:{RESET}")
    for p in metrics["processes"]:
        name = (p["name"] or "unknown")[:20]
        cpu  = p["cpu_percent"] or 0
        print(f"    PID {p['pid']:>6} │ {name:<22} │ CPU: {cpu:.1f}%")

    # ── Alerts ───────────────────────────────
    if alerts:
        print(f"\n  {BOLD}{RED}⚠  ALERTS DETECTED:{RESET}")
        for alert in alerts:
            icon = "🔴" if alert["level"] == "CRITICAL" else "🟡"
            print(f"\n  {icon} [{alert['level']}] {alert['resource']}")
            print(f"     {alert['message']}")
        save_log(metrics, alerts)
    else:
        print(f"\n  {GREEN}{BOLD}✅  System is healthy. No issues detected.{RESET}")

    print(f"\n  {CYAN}Next check in {CHECK_INTERVAL}s ... (Ctrl+C to stop){RESET}\n")

def save_log(metrics, alerts):
    """Append alert details to the health log file."""
    with open(LOG_FILE, "a") as f:
        f.write(f"\n{'='*50}\n")
        f.write(f"Timestamp : {metrics['timestamp']}\n")
        f.write(f"CPU       : {metrics['cpu']}%\n")
        f.write(f"RAM       : {metrics['ram']}%\n")
        f.write(f"Disk      : {metrics['disk']}%\n")
        f.write(f"Alerts    :\n")
        for alert in alerts:
            f.write(f"  [{alert['level']}] {alert['resource']}: {alert['message']}\n")
    print(f"  📁 Log saved to '{LOG_FILE}'")

# ─────────────────────────────────────────────
#  MAIN — Continuous Agentic Loop
# ─────────────────────────────────────────────
def main():
    print(f"{BOLD}{CYAN}Starting AI System Health Guardian...{RESET}")
    time.sleep(1)

    try:
        while True:
            metrics = observe()          # Step 1: OBSERVE
            alerts  = think(metrics)     # Step 2: THINK
            act(metrics, alerts)         # Step 3: ACT
            time.sleep(CHECK_INTERVAL)

    except KeyboardInterrupt:
        print(f"\n{YELLOW}Guardian stopped by user. Stay healthy! 👋{RESET}\n")

if __name__ == "__main__":
    main()

"""
AI System Health Guardian
An intelligent Python-based system monitoring agent.

Observe  -> Collect CPU, RAM, Disk and process information
Think    -> Decide if the system is healthy or unhealthy using rules
Act      -> Show alerts, save logs, and suggest actions
"""

import os
import time
import csv
from datetime import datetime

try:
    import psutil
except ImportError:
    print("psutil is not installed. Please run: pip install psutil")
    raise SystemExit


class AISystemHealthGuardian:
    def __init__(
        self,
        cpu_limit=80,
        ram_limit=80,
        disk_limit=90,
        check_interval=5,
        log_file="system_health_log.txt",
        csv_file="system_health_report.csv",
    ):
        self.cpu_limit = cpu_limit
        self.ram_limit = ram_limit
        self.disk_limit = disk_limit
        self.check_interval = check_interval
        self.log_file = log_file
        self.csv_file = csv_file
        self.create_csv_header()

    def create_csv_header(self):
        """Create CSV file with headers if it does not exist."""
        if not os.path.exists(self.csv_file):
            with open(self.csv_file, "w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow([
                    "Time",
                    "CPU Usage (%)",
                    "RAM Usage (%)",
                    "Disk Usage (%)",
                    "Status",
                    "Messages",
                ])

    def observe(self):
        """Observe system resource usage."""
        cpu_usage = psutil.cpu_percent(interval=1)
        ram_usage = psutil.virtual_memory().percent
        disk_usage = psutil.disk_usage("/").percent

        return {
            "cpu": cpu_usage,
            "ram": ram_usage,
            "disk": disk_usage,
        }

    def think(self, system_data):
        """Make a decision based on threshold rules."""
        warnings = []
        suggestions = []

        if system_data["cpu"] >= self.cpu_limit:
            warnings.append(f"High CPU usage detected: {system_data['cpu']}%")
            suggestions.append("Close heavy applications or browser tabs.")

        if system_data["ram"] >= self.ram_limit:
            warnings.append(f"High RAM usage detected: {system_data['ram']}%")
            suggestions.append("Close unused applications to free memory.")

        if system_data["disk"] >= self.disk_limit:
            warnings.append(f"High disk usage detected: {system_data['disk']}%")
            suggestions.append("Delete unnecessary files or move files to external/cloud storage.")

        if warnings:
            return "WARNING", warnings, suggestions

        return "HEALTHY", ["System is running normally."], ["No action needed."]

    def get_top_processes(self, limit=5):
        """Return top memory-consuming processes."""
        processes = []

        for process in psutil.process_iter(["pid", "name", "memory_percent", "cpu_percent"]):
            try:
                info = process.info
                if info["memory_percent"] is not None:
                    processes.append(info)
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                continue

        processes.sort(key=lambda x: x["memory_percent"], reverse=True)
        return processes[:limit]

    def act(self, system_data, status, messages, suggestions):
        """Display alert and save logs."""
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        print("\n" + "=" * 60)
        print("AI SYSTEM HEALTH GUARDIAN")
        print("=" * 60)
        print(f"Time        : {current_time}")
        print(f"CPU Usage   : {system_data['cpu']}%")
        print(f"RAM Usage   : {system_data['ram']}%")
        print(f"Disk Usage  : {system_data['disk']}%")
        print(f"Status      : {status}")

        print("\nAgent Messages:")
        for message in messages:
            print(f"- {message}")

        print("\nSuggested Actions:")
        for suggestion in suggestions:
            print(f"- {suggestion}")

        if status == "WARNING":
            print("\nTop 5 Memory-Consuming Processes:")
            print("-" * 60)
            for process in self.get_top_processes():
                print(
                    f"PID: {process['pid']} | "
                    f"Name: {process['name']} | "
                    f"Memory: {process['memory_percent']:.2f}%"
                )

        self.save_text_log(current_time, system_data, status, messages, suggestions)
        self.save_csv_log(current_time, system_data, status, messages)

    def save_text_log(self, current_time, system_data, status, messages, suggestions):
        """Save human-readable log file."""
        with open(self.log_file, "a", encoding="utf-8") as file:
            file.write("\n" + "=" * 60 + "\n")
            file.write(f"Time        : {current_time}\n")
            file.write(f"CPU Usage   : {system_data['cpu']}%\n")
            file.write(f"RAM Usage   : {system_data['ram']}%\n")
            file.write(f"Disk Usage  : {system_data['disk']}%\n")
            file.write(f"Status      : {status}\n")
            file.write("Agent Messages:\n")
            for message in messages:
                file.write(f"- {message}\n")
            file.write("Suggested Actions:\n")
            for suggestion in suggestions:
                file.write(f"- {suggestion}\n")

    def save_csv_log(self, current_time, system_data, status, messages):
        """Save structured CSV report."""
        with open(self.csv_file, "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([
                current_time,
                system_data["cpu"],
                system_data["ram"],
                system_data["disk"],
                status,
                " | ".join(messages),
            ])

    def run(self):
        """Main Observe -> Think -> Act loop."""
        print("Starting AI System Health Guardian...")
        print("Press CTRL + C to stop the agent.")

        try:
            while True:
                system_data = self.observe()
                status, messages, suggestions = self.think(system_data)
                self.act(system_data, status, messages, suggestions)
                time.sleep(self.check_interval)
        except KeyboardInterrupt:
            print("\nAI System Health Guardian stopped by user.")
            print(f"Text log saved as: {self.log_file}")
            print(f"CSV report saved as: {self.csv_file}")


if __name__ == "__main__":
    guardian = AISystemHealthGuardian()
    guardian.run()

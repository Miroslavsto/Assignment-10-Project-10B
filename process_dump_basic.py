# process_dump_basic.py
# Simple Process Dumping Script for DFIR
# Requires: psutil (pip install psutil)

import psutil
from datetime import datetime

def dump_processes():
    """Collect and display running processes."""
    print(f"Process Dump - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    print(f"{'PID':<10}{'Process Name':<30}{'Username':<20}")

    for proc in psutil.process_iter(['pid', 'name', 'username']):
        try:
            info = proc.info
            print(f"{info['pid']:<10}{info['name']:<30}{info['username']:<20}")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

if __name__ == "__main__":
    dump_processes()

import subprocess
from utils.logger import print_result

def check_firewall():
    """Check if firewalld is active (Standard for Rocky Linux)."""
    try:
        result = subprocess.run(
            ['systemctl', 'is-active', 'firewalld'],
            capture_output=True, text=True
        )
        if result.stdout.strip() == "active":
            print_result("PASS", "Firewall (firewalld) is active and running.")
        else:
            print_result("FAIL", "Firewall (firewalld) is NOT active.")
    except FileNotFoundError:
        print_result("WARN", "systemctl command not found.")

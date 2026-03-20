import os
import subprocess
from utils.logger import print_result

def check_failed_logins():
    """Check for excessive failed logins in /var/log/secure."""
    log_file = "/var/log/secure"
    if not os.path.exists(log_file):
        print_result("WARN", f"{log_file} not found. Are you on Rocky/RHEL?")
        return

    try:
        result = subprocess.run(
            ['grep', 'Failed password', log_file],
            capture_output=True, text=True
        )
        failed_count = len(result.stdout.strip().split('\n')) if result.stdout.strip() else 0

        if failed_count > 50:
            print_result("FAIL", f"High number of failed logins detected ({failed_count} attempts).")
        elif failed_count > 0:
            print_result("WARN", f"Some failed logins detected ({failed_count} attempts).")
        else:
            print_result("PASS", "No recent failed password attempts found.")
    except Exception as e:
        print_result("WARN", f"Could not parse auth logs: {e}")

def check_empty_passwords():
    """Check /etc/shadow for accounts with empty passwords."""
    try:
        with open("/etc/shadow", "r") as f:
            empty_pw_users = []
            for line in f:
                parts = line.split(":")
                if len(parts) > 1 and parts[1] == "":
                    empty_pw_users.append(parts[0])

            if empty_pw_users:
                print_result("FAIL", f"Users with empty passwords: {', '.join(empty_pw_users)}")
            else:
                print_result("PASS", "No users with empty passwords.")
    except PermissionError:
        print_result("FAIL", "Permission denied reading /etc/shadow.")

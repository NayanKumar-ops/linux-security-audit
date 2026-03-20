import re
from utils.logger import print_result

def check_ssh_config():
    """Audit sshd_config for PermitRootLogin and PasswordAuthentication."""
    config_file = "/etc/ssh/sshd_config"
    try:
        with open(config_file, "r") as f:
            content = f.read()

            # Check Root Login
            if re.search(r"^PermitRootLogin\s+yes", content, re.MULTILINE):
                print_result("FAIL", "SSH: Root login is permitted.")
            else:
                print_result("PASS", "SSH: Root login is restricted.")

            # Check Password Authentication
            if re.search(r"^PasswordAuthentication\s+yes", content, re.MULTILINE):
                print_result("WARN", "SSH: Password authentication is enabled (Keys are safer).")
            else:
                print_result("PASS", "SSH: Password authentication is disabled.")

    except FileNotFoundError:
        print_result("WARN", f"{config_file} not found.")

import subprocess
from utils.logger import print_result

def check_updates():
    """Check if dnf-automatic is enabled for unattended upgrades."""
    try:
        result = subprocess.run(
            ['systemctl', 'is-enabled', 'dnf-automatic.timer'],
            capture_output=True, text=True
        )
        if result.stdout.strip() == "enabled":
            print_result("PASS", "Unattended upgrades (dnf-automatic) are enabled.")
        else:
            print_result("WARN", "Unattended upgrades (dnf-automatic) are NOT enabled.")
    except Exception:
        print_result("WARN", "Could not verify dnf-automatic status.")

#!/usr/bin/env python3

import os
import sys

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from utils.colors import RED, RESET
from modules import (
    check_failed_logins,
    check_empty_passwords,
    check_ssh_config,
    check_firewall,
    check_updates,
)

def check_root():
    """Ensure the script is run as root."""
    if os.geteuid() != 0:
        print(f"[{RED} ERROR {RESET}] This script must be run as root.")
        sys.exit(1)

def main():
    print("\n========================================")
    print("   ROCKY LINUX SECURITY SCANNER v1.0   ")
    print("========================================\n")

    check_root()

    print("--- User Audit ---")
    check_failed_logins()
    check_empty_passwords()

    print("\n--- SSH Audit ---")
    check_ssh_config()

    print("\n--- Network Audit ---")
    check_firewall()

    print("\n--- Package Audit ---")
    check_updates()

    print("\n========================================")
    print("            AUDIT COMPLETE              ")
    print("========================================\n")

if __name__ == "__main__":
    main()

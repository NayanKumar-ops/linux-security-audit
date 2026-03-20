<div align="center">

# 🛡️ Linux Security Audit

> **Automated security hardening scanner for Rocky Linux / RHEL systems.**  
> Built for sysadmins, DevOps engineers, and security-minded developers.

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Platform](https://img.shields.io/badge/Platform-Rocky%20Linux-green?style=for-the-badge&logo=linux)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)

</div>

---

## 📌 What is This?

`linux-security-audit` is a **modular, terminal-based security scanner** that automatically checks your Linux system for common vulnerabilities and misconfigurations.

No external tools. No bloat. Just Python and the truth about your system.

---

## ⚡ Features

| Check | Description | Status |
|---|---|---|
| 🔐 Failed Logins | Detects brute-force attempts via `/var/log/secure` | ✅ Active |
| 👤 Empty Passwords | Scans `/etc/shadow` for passwordless accounts | ✅ Active |
| 🔑 SSH Hardening | Checks `PermitRootLogin` & `PasswordAuthentication` | ✅ Active |
| 🔥 Firewall Status | Verifies `firewalld` is running | ✅ Active |
| 📦 Auto Updates | Checks if `dnf-automatic` is enabled | ✅ Active |

---

## 🗂️ Project Structure
```
linux-security-audit/
├── audit.py                  # Main entry point
├── modules/
│   ├── __init__.py
│   ├── user_audit.py         # Failed logins & empty passwords
│   ├── ssh_audit.py          # SSH config hardening
│   ├── network_audit.py      # Firewall checks
│   └── package_audit.py      # Update verification
├── utils/
│   ├── __init__.py
│   ├── colors.py             # Terminal colors
│   └── logger.py             # PASS / FAIL / WARN output
├── config/
│   └── audit_config.yaml     # Enable/disable checks
├── reports/                  # Saved audit reports
├── requirements.txt
└── .gitignore
```

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/NayanKumar-ops/linux-security-audit.git
cd linux-security-audit
```

### 2. Run the Scanner
```bash
sudo python3 audit.py
```

> ⚠️ Must be run as **root** to access system logs and shadow file.

---

## 🖥️ Sample Output
```
========================================
   ROCKY LINUX SECURITY SCANNER v1.0
========================================

--- User Audit ---
[ PASS ] No recent failed password attempts found.
[ PASS ] No users with empty passwords.

--- SSH Audit ---
[ FAIL ] SSH: Root login is permitted.
[ WARN ] SSH: Password authentication is enabled (Keys are safer).

--- Network Audit ---
[ FAIL ] Firewall (firewalld) is NOT active.

--- Package Audit ---
[ WARN ] Unattended upgrades (dnf-automatic) are NOT enabled.

========================================
            AUDIT COMPLETE
========================================
```

---

## 🛠️ Requirements

- Rocky Linux 8/9 or RHEL-based distro
- Python 3.x
- Root / sudo access
- No external Python packages needed

---

## 🔮 Roadmap

- [ ] HTML report generation
- [ ] Email alerts on FAIL
- [ ] Cron job auto-scheduling
- [ ] CIS Benchmark integration
- [ ] Kernel hardening checks

---

## 👤 Author

**NayanKumar-ops**  
📧 nayankumar.ops@gmail.com  
🐙 [github.com/NayanKumar-ops](https://github.com/NayanKumar-ops)

---

<div align="center">

**⭐ Star this repo if it helped you.**  
*Built with focus. No shortcuts.*

</div>

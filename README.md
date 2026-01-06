# ReconX
Enumeration wins the battle before exploitation begins 🔎⚔️
Built a controlled lab environment using Kali Linux (attacker) and Ubuntu (target) configured on a NAT-only virtual network.
This setup ensured isolated host-only communication for safe security testing and traffic analysis.
# Python-Based Directory Enumeration Tool (NGINX Lab)

# Project Description
Built a Python-based directory enumeration tool and tested it against an NGINX web server in a controlled lab environment. Created custom directories to simulate exposed endpoints and validated results through HTTP response analysis.

# Tool Features
Directory enumeration using wordlists
Detects HTTP 200 (OK) responses
Detects HTTP 403 (Forbidden) responses
# OUTPUT

# PROJECT 2: Authentication Weakness Detection Using Nmap NSE

# Project Description
Detect weak or misconfigured authentication (FTP, SSH)
Identified weak or misconfigured authentication in FTP and SSH using Nmap NSE scripts
Detected anonymous FTP access and multiple SSH authentication methods
Highlighted risk of unauthorized access and brute-force attacks, validated via NSE scan results

# 🔐 SSH Brute-Force Detection (Safe Lab)

# Project Overview
This project demonstrates the detection of weak or misconfigured SSH authentication in a controlled lab environment using Nmap NSE scripts and system logs 🖥️. The assessment identifies risks such as password-based authentication and keyboard-interactive methods, which can allow brute-force attacks ⚠️.

# 🛠️ Tools Used
Kali Linux (Attacker) 🐧
Ubuntu Server (Target) 🖥️
Nmap NSE scripts (ssh-auth-methods) 🔍
System logs (/var/log/auth.log) 📄

📋 Steps

# 1.Scan SSH service using Nmap NSE:

nmap -p 22 --script ssh-auth-methods <target-ip>

# 2.Observe authentication methods detected (publickey, password, keyboard-interactive) 🔑

# 3.Simulate brute-force attempts (safe lab only) using Hydra with a small password list:

hydra -l testuser -P password-list.txt ssh://<target-ip> -t 4
Monitor /var/log/auth.log on the target to detect failed login attempts 📈

# 📌 Findings

Password and keyboard-interactive authentication detected on SSH service 🔓
Multiple failed login attempts observed in system logs, indicating brute-force risk ⚠️

# 📸 Screenshots

screenshots/ssh-nse-output.png → NSE detection output
screenshots/auth-log-detection.png → Auth log detection

# 🛡️ Mitigation Recommendations
Enforce key-based SSH authentication 🔑
Disable password and keyboard-interactive authentication ❌
Implement rate-limiting or Fail2Ban to block brute-force attempts ⛔



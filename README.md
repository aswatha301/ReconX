# 🔎 ReconX: Web Enumeration, Authentication Weakness & SSH Attack Detection Lab

# 🧩 Project Overview
This project demonstrates a comprehensive reconnaissance and authentication security assessment conducted in a controlled lab environment 🧪. The assessment covers web directory enumeration, authentication weakness detection in FTP and SSH, and SSH brute‑force activity detection 🔐. Using Nmap NSE scripts, custom tools, and system logs, the project highlights how insecure configurations can be identified before exploitation begins ⚠️. All testing was performed in an isolated NAT‑based virtual network to ensure safe and ethical security analysis 🛡️.

# 🛠️ Tools Used

🐧 Kali Linux (Attacker)

🖥️ Ubuntu Server (Target)

🔍 Nmap with NSE scripts

🐍 Python (Directory Enumeration Tool)

🌐 NGINX Web Server

📄 System Logs (/var/log/auth.log)

⚔️ Hydra (Safe lab usage)

# ⚙️ Steps Performed

🔎 Web Directory Enumeration (NGINX Lab)

# python3 dir_enum.py

Validated exposed endpoints using HTTP response codes (200 / 403).

🔐 Authentication Weakness Detection (FTP & SSH)

# nmap -p 21 --script ftp-anon <target-ip>

# nmap -p 22 --script ssh-auth-methods <target-ip>

Detected anonymous FTP access and multiple SSH authentication methods.

⚔️ SSH Brute‑Force Activity Detection (Safe Lab)

# hydra -l testuser -P password-list.txt ssh://<target-ip> -t 4

Observed repeated failed login attempts via authentication logs.

# 📌 Findings

🚨 Anonymous authentication detected in FTP service

🔓 Multiple SSH authentication methods enabled (password, keyboard‑interactive)

📈 Repeated failed SSH login attempts observed in system logs

⚠️ Increased risk of unauthorized access and brute‑force attacks

# 📸 Screenshots

🖼️ Nmap NSE scan outputs (FTP & SSH detection)

🖼️ Python directory enumeration results

🖼️ SSH authentication log entries showing failed attempts

# 🛡️ Mitigation Recommendations

🔑 Disable anonymous FTP access

🔐 Enforce key‑based SSH authentication

🚫 Disable password and keyboard‑interactive SSH methods

⛔ Implement rate‑limiting and Fail2Ban for SSH protection


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

![dir](https://github.com/user-attachments/assets/a6eb14e7-6ca0-416f-8bf6-f0171eb2d71b)


Validated exposed endpoints using HTTP response codes (200 / 403).

🔐 Authentication Weakness Detection (FTP & SSH)

# nmap -p 21 --script ftp-anon <target-ip>

![ftp](https://github.com/user-attachments/assets/daedac26-e8a4-419a-8e19-59dcd59703c6)

![ftp2](https://github.com/user-attachments/assets/6a073484-d984-4132-85fe-186f3ee2a11d)



# nmap -p 22 --script ssh-auth-methods <target-ip>

![ssh2](https://github.com/user-attachments/assets/8a591e79-6ca6-48e0-8a5b-6345d296e867)

Detected multiple SSH authentication methods.

⚔️ SSH Brute‑Force Activity Detection (Safe Lab)

# hydra -l testuser -P password-list.txt ssh://<target-ip> -t 4

![kk](https://github.com/user-attachments/assets/783f31cb-e203-48f5-bbe3-e1b21eec9dab)

![kk1](https://github.com/user-attachments/assets/c6ffcac0-c3fd-4951-86e6-e2690190707d)

Observed repeated failed login attempts via authentication logs.

![kk2](https://github.com/user-attachments/assets/d58bf398-8b46-4bf2-9be4-fbd5f211f34b)


# 📌 Findings

🚨 Anonymous authentication detected in FTP service

🔓 Multiple SSH authentication methods enabled (password, keyboard‑interactive)

📈 Repeated failed SSH login attempts observed in system logs

⚠️ Increased risk of unauthorized access and brute‑force attacks

# 🛡️ Mitigation Recommendations

🔑 Disable anonymous FTP access

🔐 Enforce key‑based SSH authentication

🚫 Disable password and keyboard‑interactive SSH methods

⛔ Implement rate‑limiting and Fail2Ban for SSH protection


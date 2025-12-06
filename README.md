# Network_Scanner
A fast multi-threaded Python network scanner that detects live hosts and open TCP ports across any IP range. Uses ICMP ping, TCP connect scanning, and optimized threading for accurate results. Supports single-IP and full subnet scans. Simple, lightweight, and effective for learning and cybersecurity projects.
🔍 Network Scanner (Python)

This project is a fast and accurate multi-threaded network scanner built using Python. It can scan entire subnets or single IP addresses to identify live hosts and open TCP ports. The tool is optimized with ICMP ping checks, socket retries, and parallel execution for high performance and reliability.

🚀 Features

🔎 Scan entire networks (ex: 192.168.1.0/24)

💻 Scan a single host (8.8.8.8/32)

🟢 Detect live hosts using ICMP ping

🔐 TCP port scanning with retry logic

⚡ Multi-threaded for high-speed scanning

🧩 Accurate results on Windows & Linux

📡 Shows open/closed ports clearly

🧵 Thread-safe queue system

🧭 Easy to use, beginner-friendly

🛠 Technologies Used

Python 3

socket → TCP connection scanning

subprocess → ICMP ping detection

threading → multi-thread concurrency

ipaddress → subnet and host parsing

queue → task distribution

📦 Installation

Install Python 3

Clone this repository:

git clone https://github.com/Sidthehacker-code/Network_scanner.git
cd <repo-name>


Run the tool:

python network_scanner.py

📝 Usage

Run the script and provide:

1️⃣ Network Range

Examples:

192.168.1.0/24
10.0.0.1/32
8.8.8.8/32

2️⃣ Port Range

Example:

Start Port: 1
End Port: 1024

📄 Sample Output
Starting scan...

[+] 192.168.1.10 is UP | Open Ports → [22, 80]
[-] 192.168.1.11 is UP | No open ports found
[x] 192.168.1.15 is DOWN

=== Scan Finished ===
Time Taken: 4.92 sec

🧪 Tested On

✔ Windows 10 / 11

✔ Kali Linux

✔ Ubuntu

✔ Python 3.10+

🔮 Future Enhancements

UDP port scanning

OS detection (fingerprinting)

Banner grabbing

Export results to CSV

Parallel multiprocessing

Web-based UI

Real-time progress bar

🤝 Contributing

Contributions, issues, and feature requests are welcome!

📜 License

This project is released under the MIT License.

If you want, I can also:

✔ Create a project logo
✔ Add GitHub badges (stars, forks, Python version)
✔ Create a better professional description
✔ Add installation screenshots

import socket
import ipaddress
import threading
import queue
import subprocess
import time

# Ping a host to verify it's alive
def is_up(ip):
    try:
        output = subprocess.check_output(
            ["ping", "-n", "1", "-w", "300", ip],  # Windows
            stderr=subprocess.DEVNULL,
            stdin=subprocess.DEVNULL
        ).decode()
        return "TTL" in output
    except:
        return False

# Scan a single TCP port
def scan_port(ip, port, retries=2, timeout=0.3):
    for _ in range(retries):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(timeout)
            result = s.connect_ex((ip, port))
            s.close()
            if result == 0:
                return True
        except:
            pass
    return False

# Scan host for open ports
def scan_host(ip):
    open_ports = []
    for port in range(start_port, end_port + 1):
        if scan_port(ip, port):
            open_ports.append(port)

    if open_ports:
        print(f"[+] {ip} is UP | Open Ports → {open_ports}")
    else:
        print(f"[-] {ip} is UP | No open ports in range")

# Worker threads
def worker():
    while not ip_queue.empty():
        ip = ip_queue.get()
        if is_up(ip):
            scan_host(ip)
        else:
            print(f"[x] {ip} is DOWN")
        ip_queue.task_done()

# ---------- MAIN PROGRAM ----------
network_input = input("Enter network : ")
ip_net = ipaddress.ip_network(network_input, strict=False)

start_port = int(input("Enter start port: "))
end_port = int(input("Enter end port: "))

ip_queue = queue.Queue()
for ip in ip_net.hosts():
    ip_queue.put(str(ip))

num_threads = 100
start_time = time.time()

print("\nStarting scan...\n")
threads = []
for _ in range(num_threads):
    t = threading.Thread(target=worker)
    t.daemon = True
    t.start()
    threads.append(t)

ip_queue.join()

print("\n=== Scan Finished ===")
print(f"Time Taken: {time.time() - start_time:.2f} sec")

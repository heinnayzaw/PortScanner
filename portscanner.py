import socket

target = input("Enter target IP or hostname: ")

print(f"Scanning {target}...")

for port in range(1, 101):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(0.5)
        result = sock.connect_ex((target, port))

        if result == 0:
            print(f"[OPEN] Port {port}")

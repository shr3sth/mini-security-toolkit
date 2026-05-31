import socket
import time


def scan_ports():
    target = input("Enter target IP or hostname: ")

    start_port = int(input("Start port: "))
    end_port = int(input("End port: "))

    open_ports = []

    print(f"\nScanning {target}...\n")

    start_time = time.time()

    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)

        result = sock.connect_ex((target, port))

        if result == 0:
            print(f"[OPEN] Port {port}")
            open_ports.append(port)

        sock.close()

    duration = round(time.time() - start_time, 2)

    print("\n--- Scan Complete ---")
    print(f"Open Ports Found: {len(open_ports)}")
    print(f"Time Taken: {duration} seconds")
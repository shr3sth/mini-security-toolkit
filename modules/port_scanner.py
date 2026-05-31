import socket
import time


def scan_ports(target, start_port, end_port):

    open_ports = []

    report = f"Scanning {target}...\n\n"

    start_time = time.time()

    for port in range(start_port, end_port + 1):

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        sock.settimeout(0.5)

        result = sock.connect_ex((target, port))

        if result == 0:
            open_ports.append(port)

        sock.close()

    duration = round(time.time() - start_time, 2)

    report += "=== Scan Complete ===\n\n"

    report += f"Open Ports Found: {len(open_ports)}\n"

    report += f"Time Taken: {duration} seconds\n\n"

    if open_ports:

        report += "Open Ports:\n"

        for port in open_ports:
            report += f"- {port}\n"

    else:
        report += "No open ports found."

    return report

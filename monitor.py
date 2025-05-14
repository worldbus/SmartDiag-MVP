# monitor.py

from ping3 import ping
import socket
import time

def run_ping_traceroute(domain: str) -> str:
    output = []
    output.append("Ping Results (RTT in ms):")

    for i in range(3):
        # 1) Try ping3 without root privileges
        try:
            rtt = ping(domain, unit="ms", timeout=2, privileged=False)
            if rtt is None:
                output.append(f"  Attempt {i+1}: timeout")
            else:
                output.append(f"  Attempt {i+1}: {rtt:.1f} ms")
            continue
        except Exception:
            pass

        # 2) Fallback: TCP handshake timing on port 80
        start = time.time()
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)
            sock.connect((domain, 80))
            sock.close()
            elapsed = (time.time() - start) * 1000
            output.append(f"  Attempt {i+1}: {elapsed:.1f} ms (TCP connect)")
        except Exception as ex:
            output.append(f"  Attempt {i+1}: error ({ex})")

    output.append("\nTraceroute: not available in this environment")
    return "\n".join(output)

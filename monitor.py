# monitor.py

from ping3 import ping
import socket

def run_ping_traceroute(domain: str) -> str:
    output = []

    # 1) Ping 3 times
    output.append("Ping Results (RTT in ms):")
    for i in range(3):
        try:
            rtt = ping(domain, unit="ms", timeout=2)
            output.append(f"  Attempt {i+1}: {rtt:.1f} ms" if rtt else f"  Attempt {i+1}: timeout")
        except Exception as e:
            output.appen

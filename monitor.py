# monitor.py
from ping3 import ping

def run_ping_traceroute(domain: str) -> str:
    output = []

    # 1) Ping 3 times
    output.append("Ping Results (RTT in ms):")
    for i in range(3):
        try:
            rtt = ping(domain, unit="ms", timeout=2)
            if rtt is None:
                output.append(f"  Attempt {i+1}: timeout")
            else:
                output.append(f"  Attempt {i+1}: {rtt:.1f} ms")
        except Exception as e:
            output.append(f"  Attempt {i+1}: error ({e})")

    # 2) Traceroute not available
    output.append("\nTraceroute: not available in this environment")

    return "\n".join(output)

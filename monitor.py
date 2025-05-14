import subprocess

def run_ping_traceroute(domain: str) -> str:
    ping = subprocess.run(
        ["ping", "-c", "3", domain],
        capture_output=True, text=True
    ).stdout
    trace = subprocess.run(
        ["traceroute", "-m", "10", domain],
        capture_output=True, text=True
    ).stdout
    return f"Ping Results:\n{ping}\nTraceroute Results:\n{trace}"

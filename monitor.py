# monitor.py
import subprocess

def run_tests(domain: str) -> dict:
    #result ping
    ping = subprocess.run(
      ["ping", "-c", "3", domain],
      capture_output=True, text=True
    ).stdout
    # result traceroute
    trace = subprocess.run(
      ["traceroute", "-m", "10", domain],
      capture_output=True, text=True
    ).stdout
    return {"ping": ping, "traceroute": trace}

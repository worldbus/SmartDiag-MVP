# monitor.py

import subprocess

def run_ping_traceroute(domain: str) -> str:
    lines = []

    # 1) Real ping
    lines.append("Ping Results:")
    try:
        ping_proc = subprocess.run(
            ["ping", "-c", "3", domain],
            capture_output=True, text=True, check=True
        )
        lines.append(ping_proc.stdout.strip())
    except subprocess.CalledProcessError as e:
        # non-zero exit code (e.g., host unreachable)
        lines.append(f"Ping failed:\n{e.stdout or e.stderr}".strip())
    except Exception as e:
        lines.append(f"Ping error: {e}")

    # 2) Real traceroute
    lines.append("\nTraceroute Results:")
    try:
        trace_proc = subprocess.run(
            ["traceroute", "-m", "10", domain],
            capture_output=True, text=True, check=True
        )
        lines.append(trace_proc.stdout.strip())
    except subprocess.CalledProcessError as e:
        lines.append(f"Traceroute failed:\n{e.stdout or e.stderr}".strip())
    except Exception as e:
        lines.append(f"Traceroute error: {e}")

    return "\n".join(lines)

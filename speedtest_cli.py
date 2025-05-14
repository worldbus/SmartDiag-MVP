import speedtest

def run_speed_test() -> dict:
    tester = speedtest.Speedtest()
    tester.get_best_server()
    download = tester.download()
    upload   = tester.upload()
    ping     = tester.results.ping
    return {
        "download_Mbps": round(download / 1e6, 1),
        "upload_Mbps":   round(upload   / 1e6, 1),
        "ping_ms":       ping
    }

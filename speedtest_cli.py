# speedtest_cli.py

import speedtest

def run_speed_test() -> dict:
    try:
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
    except speedtest.ConfigRetrievalError:
        return {"error": "Could not retrieve speedtest config"}
    except Exception as e:
        return {"error": str(e)}

import requests, time

# list of URLs to ping
URLS = [
    "https://server.speedyutils.com",
    "https://utils.speedyutils.com",
]

# run for 4 minutes → 4 requests (1/min)
INTERVAL_SECONDS = 60
TOTAL_MINUTES = 4

def send_requests():
    for minute in range(TOTAL_MINUTES):
        for url in URLS:
            try:
                # fire and forget (don't wait for response content)
                requests.get(url, timeout=5)
            except Exception:
                pass  # ignore all errors completely
        time.sleep(INTERVAL_SECONDS)

if __name__ == "__main__":
    send_requests()

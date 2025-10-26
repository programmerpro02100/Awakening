import requests, time

URLS = [
    "https://server.speedyutils.com",
    "https://utils.speedyutils.com",
]

INTERVAL_SECONDS = 60  # one request every minute

def loop_forever():
    while True:
        for url in URLS:
            try:
                requests.get(url, timeout=5)
            except Exception:
                pass  # ignore all errors
        time.sleep(INTERVAL_SECONDS)

if __name__ == "__main__":
    loop_forever()

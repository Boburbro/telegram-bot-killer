import urllib.request
import urllib.parse
import time
import random
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.error import HTTPError

MAX_WORKERS = 20        
START_RATE = 1000       
RATE_STEP = 10        
MAX_RATE = 20000
TIMEOUT = 0.1

def send_message(i: int) -> bool:
    payload = {
        "chat_id": random.randint(1000000000, 9999999999),
        "text": f"Realtime load msg #{i} | {random.randint(1000,9999)}"
    }

    data = urllib.parse.urlencode(payload).encode("utf-8")
    req = urllib.request.Request(API_URL, data=data, method="POST")

    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT):
            return True
    except HTTPError as e:
        if e.code == 429:
            return False
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False


def now():
    return time.strftime("%H:%M:%S")


def main():
    rate = START_RATE
    msg_counter = 0

    print("🚀 Real-time Telegram load test started\n")

    while True:
        start_ts = time.time()
        success = 0
        fail = 0

        with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
            futures = [
                executor.submit(send_message, msg_counter + i)
                for i in range(rate)
            ]

            for f in as_completed(futures):
                if f.result():
                    success += 1
                else:
                    fail += 1

        msg_counter += rate

        print(f"{now()}  sent={success}  fail={fail}  target={rate}")

        # Agar fail ko‘paysa – rate tushiramiz
        if fail > success:
            rate = max(5, rate // 2)
        else:
            rate = min(rate + RATE_STEP, MAX_RATE)

        # sekundni to‘ldirish
        elapsed = time.time() - start_ts
        if elapsed < 1:
            time.sleep(1 - elapsed)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Telegram bot load tester")
    parser.add_argument("--token", required=True, help="Telegram bot token")
    args = parser.parse_args()
    TOKEN = args.token
    API_URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    main()

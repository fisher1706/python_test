import time
from multiprocessing import Process

import requests


def activity():
    # result = 0
    # for e in range(1000_000):
    #     result += abs(round(e ** 2 / 122) + e * 3.14)
    # print(result)

    requests.get("https://google.com")
    print("ok")


def run(parallel=True):
    start = time.time()
    if not parallel:
        for e in range(10):
            activity()
    else:
        processes = [Process(target=activity, daemon=True) for _ in range(10)]
        for e in processes:
            e.start()
        for e in processes:
            e.join()

    end = time.time()
    print(f"time: {end - start} seconds")


if __name__ == '__main__':
    run(parallel=False)
    run()

import threading
import time
from threading import Thread

counter = [0]
lock = threading.Lock()


def inc():
    lock.acquire()
    c = counter[0]
    time.sleep(0.1)
    counter[0] = c + 1
    lock.release()


if __name__ == "__main__":
    threads = [Thread(target=inc, daemon=True) for _ in range(10)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print(counter)

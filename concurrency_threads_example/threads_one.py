import os
import threading
from threading import Thread


def info():
    pid = os.getpid()
    name = threading.current_thread().name
    print(f"Process - {pid}, name - {name}")


if __name__ == "__main__":
    # info()

    threads = [Thread(target=info, daemon=True) for _ in range(10)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

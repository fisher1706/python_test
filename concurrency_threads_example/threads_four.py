import time
from queue import Queue
from threading import Thread

queue = Queue()
queue.put(0)


def inc_queue():
    c = queue.get()
    time.sleep(0.1)
    queue.put(c + 1)


if __name__ == "__main__":
    threads = [Thread(target=inc_queue, daemon=True) for _ in range(10)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print(queue.qsize())
    print(queue.get_nowait())

import threading
import time
from concurrent.futures import ThreadPoolExecutor

import requests



"""
Конкурентность - запуск на выполнение сразу нескольких задач
(не обязательно в один момент времени выполняется несколько)
Зависит от ПО

Параллельность - конкурентность, когда 2+ задачи выполняются одновременно, зависит от железа.

thread-safe - потокобезобастность - при работе с объектом не возникают проблемы с конкурентностью
GIL - глобальная блокировка интепретатора

Задачи могут быть:
- CPU-bound - зависит от мощности процессора
- IO-bound - зависит от системы ввода/вывода


threading - IO-bound задачи
asyncio - IO-bound задачи
multiprocessing - любые задачи
"""


def activity():
    # for e in range(1000_000):
    #     abs(round(e ** 2 / 122) + e * 3.14)

    requests.get(url='https://google.com')

    print("Ok")


def run(treading=False):
    start = time.time()
    if not treading:
        for e in range(10):
            activity()
    else:
        executor = ThreadPoolExecutor()
        for _ in range(10):
            executor.submit(activity)
        executor.shutdown(wait=True)

        # threads = [threading.Thread(target=activity, daemon=True) for _ in range(10)]
        # for e in threads:
        #     e.start()
        #     print(f"{e} - start")
        # for e in threads:
        #     e.join()
        #     print(f"{e} - join")

    end = time.time()
    print(f"Time: {end - start} seconds")


if __name__ == '__main__':
    run(treading=True)
    run()

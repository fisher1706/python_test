import time
from multiprocessing import Process, Pool


def work():
    arr = list(range(1000_000))
    step = len(arr) // 10
    position = 0
    processes = []
    for _ in range(10):
        split = arr[position:position + step]
        processes.append(Process(target=calc_sum_print, args=(split,), daemon=True))
        position += step
    start = time.time()
    for e in processes:
        e.start()
    for e in processes:
        e.join()
    end = time.time()
    print(f"time: {end - start} seconds")


def work_pool():
    arr = list(range(1000_000))
    step = len(arr) // 10
    start = time.time()
    with Pool(processes=10) as pool:
        result = pool.map(calc_sum, [arr[position:position + step] for position in range(0, len(arr), step)])
        print(result)
    end = time.time()
    print(f"time: {end - start} seconds")


def calc_sum(a_list: list):
    return sum(a_list)


def calc_sum_print(a_list: list):
    print(sum(a_list))


if __name__ == '__main__':
    work()
    work_pool()

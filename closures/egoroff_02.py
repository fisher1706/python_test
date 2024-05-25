# https://www.youtube.com/watch?v=vrkLShOYwI0&list=PLQAt0m1f9OHvv2wxPGSCWjgy1qER_FvB6&index=66

from time import perf_counter


def average_number():
    summ = 0
    count = 0

    def inner(number):
        nonlocal summ, count
        summ += number
        count += 1
        return summ / count

    return inner


def timer():
    start = perf_counter()

    def inner():
        return perf_counter() - start

    return inner


def add(a, b):
    return a + b


def counter(func):
    count = 0

    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print(f"func {func.__name__} open {count}")
        return func(*args, **kwargs)

    return inner


if __name__ == "__main__":
    r1 = average_number()
    print(f"r1: {r1}")
    print(f"average: {r1(5)}")
    print(f"average: {r1(10)}")
    print("*" * 200)

    t = timer()
    print(f"time: {t()}")
    print(f"time: {t()}")
    print("*" * 200)

    c = counter(add)
    print(f"c: {c}")
    print(f"result: {c(1, 1)}")
    print(f"result: {c(1, 3)}")

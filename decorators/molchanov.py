# https://www.youtube.com/watch?v=Ss1M32pp5Ew

from datetime import datetime


def time_one(func):
    def wrapper_one(*args):
        start = datetime.now()
        result = func(*args)
        print(f"time_one: {datetime.now() - start}")
        return result

    return wrapper_one


def time_two(arg):
    def outer(func):
        def wrapper(*args):
            print(f"arg: {arg}")
            start = datetime.now()
            result = func(*args)
            print(f"time_two: {datetime.now() - start}")
            return result

        return wrapper

    return outer


def one(n):
    data = [x for x in range(10**n) if x % 2 == 0]
    print(f"data: {data}")
    return data


@time_one
def two(n):
    data = [x for x in range(10**n) if x % 2 == 0]
    print(f"data: {data}")
    return data


@time_two("zapel")
def three(n):
    data = [x for x in range(10**n) if x % 2 == 0]
    print(f"data: {data}")
    return data


if __name__ == "__main__":
    one(2)
    print("*" * 250)

    two(2)
    print("*" * 250)

    l2 = time_one(one)
    print(type(l2), l2.__name__)
    c = time_one(one)(2)
    print("*" * 250)

    three(2)

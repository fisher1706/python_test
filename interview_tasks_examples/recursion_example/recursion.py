"""
Рекурсия ограничена глубиной стека - (1000 - по умолчанию), не оптимизирована
"""

import sys


def inc_with_error(x):
    print(x)
    return inc_with_error(x + 1)


def my_sum(a_list: list) -> int:
    if not a_list:
        return 0
    if len(a_list) == 1:
        return a_list[0]
    return a_list[0] + my_sum(a_list[1:])


def my_reverse(value: str = "hello") -> str:
    if not value:
        return ""
    if len(value) == 1:
        return value
    if len(value) == 2:
        return f"{value[1]}{value[0]}"
    return my_reverse(value[1:]) + value[0]


def my_pow(x: int, y: int) -> int:
    if y == 0:
        return 1
    if y == 1:
        return x
    if y == 2:
        return x * x
    return x * my_pow(x, y - 1)


if __name__ == "__main__":
    data = my_sum([1, 2, 3, 4, 5])
    print(data)

    print(my_reverse())
    print(my_pow(2, 4))

    # get recursion limit
    print(sys.getrecursionlimit())

    # set recursion limit
    print(sys.setrecursionlimit(2000))

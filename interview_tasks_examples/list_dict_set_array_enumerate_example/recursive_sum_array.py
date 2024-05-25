# https://www.youtube.com/watch?v=euoN2zO7zao&list=PLysMDSbb9Hcyxwq966ET1_6dXkNF_PW0L&index=2


import asyncio
import nest_asyncio

nest_asyncio.apply()


def recursive_sum_one(array):
    global amount
    iterable = []

    for el in array:
        if hasattr(el, "__iter__"):
            iterable.append(el)
        elif type(el) in [int, float]:
            amount += el

    for el in iterable:
        recursive_sum_one(el)


def recursive_sum_two(*args):
    total_sum = 0
    for arg in args:
        if hasattr(arg, "__iter__") and not isinstance(
            arg, str
        ):  # check if [arg] iterable and not str
            total_sum += recursive_sum_two(*arg)
        elif isinstance(arg, (int, float)):
            total_sum += arg
    return total_sum


def recursive_sum_three(*args, path=[]):
    total_sum = 0
    for index, arg in enumerate(args):
        if hasattr(arg, "__iter__") and not isinstance(
            arg, str
        ):  # check if [arg] iterable and not str
            total_sum += recursive_sum_three(*arg, path=path + [index])
        elif isinstance(arg, (int, float)):
            total_sum += arg
        elif isinstance(arg, str):
            print(f"str '{arg}' on position", "".join(f"[{n}]" for n in path + [index]))
    return total_sum


async def recursive_sum_four(*args, path=[]):
    total_sum = 0
    for index, arg in enumerate(args):
        if hasattr(arg, "__iter__") and not isinstance(
            arg, str
        ):  # check if [arg] iterable and not str
            total_sum += await recursive_sum_four(*arg, path=path + [index])
        elif isinstance(arg, (int, float)):
            total_sum += arg
        elif isinstance(arg, str):
            print(f"str '{arg}' on position", "".join(f"[{n}]" for n in path + [index]))
    return total_sum


if __name__ == "__main__":
    data = [1, 2, "abc", [3, 4, (5, 7), 6, {7, "xyz"}, 8], 1]
    # amount = 0
    #
    # recursive_sum_one(data)
    #
    # print(amount)

    out = recursive_sum_two(data)
    print(out)

    out_two = recursive_sum_three(*data)

    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(recursive_sum_four(*data))
    print(result)

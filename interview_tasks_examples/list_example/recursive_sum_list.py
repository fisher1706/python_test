# https://www.youtube.com/watch?v=euoN2zO7zao&list=PLysMDSbb9Hcyxwq966ET1_6dXkNF_PW0L&index=2


def recursive_sum(*args, path: list[int] = None):
    path = [] if path is None else path
    total_sum = 0

    for index, arg in enumerate(args):
        if hasattr(arg, "__iter__") and not isinstance(arg, str):  # check if [arg] iterable and not str
            total_sum += recursive_sum(*arg, path=path + [index])
        elif isinstance(arg, (int, float)):
            total_sum += arg
        elif isinstance(arg, str):
            print(f"str '{arg}' on position", "".join(f"[{n}]" for n in path + [index]))
    return total_sum


if __name__ == "__main__":
    data = [1, 2, "abc", [3, 4, (5, 7), 6, {7, "xyz"}, 8], 1]

    out = recursive_sum(data)
    print(out)

    print("*" * 100)
    a = []
    b = [1]
    c = [2]
    print(a + b + c)  # [1, 2]

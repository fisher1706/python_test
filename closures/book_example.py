def func1():
    a = 1
    b = "line"
    c = [1, 2, 3]

    def func2():
        nonlocal a
        c.append(4)
        a = a + 1
        return a, b, c

    return func2


def countdown(n):
    def step():
        nonlocal n
        r = n
        n -= 1
        return r

    return step


if __name__ == "__main__":
    calc_func = func1()

    for item in calc_func.__closure__:
        print(item)

    do_step = countdown(5)

    print(do_step())
    print(do_step())

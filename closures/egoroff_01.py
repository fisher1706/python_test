# https://www.youtube.com/watch?v=lA979PBb0TY


def main_func_one():
    def inner_func():
        print('hello my friend')

    inner_func()


def main_func_two(name):
    def inner_func():
        print('hello my friend', name)

    return inner_func


def adder(value):
    def inner(var):
        return value + var

    return inner


def counter():
    count = 0

    def inner():
        nonlocal count
        count += 1
        return count

    return inner


if __name__ == '__main__':
    print(f"a: {main_func_one()}")
    print("*" * 200)

    b = main_func_two('oleg')
    print(f"b: {b}")
    b()
    print("*" * 200)

    c = adder(10)
    print(f"c: {c(5)}")
    print("*" * 200)

    d = counter()
    print(f"d: {d()}")
    print(f"d: {d()}")

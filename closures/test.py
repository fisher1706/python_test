# https://www.youtube.com/watch?v=lA979PBb0TY

def main_func_0():
    def inner_func():
        print('hello my friend')

    inner_func()

def main_func_1(name):
    def inner_func():
        print('hello my friend', name)
    return inner_func

# name = 'Ivan'
#
# def inner_func_1():
#     print('hello my friend', name)


def adder(value):
    def inner(a):
        return value + a
    return inner

def counter():
    count = 0
    def inner():
        nonlocal count
        count += 1
        return count
    return inner



if __name__ == '__main__':
    pass
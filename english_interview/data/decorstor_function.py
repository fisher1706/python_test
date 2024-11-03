"""
Decorators modify the behavior of a function or method.
"""


def outer(func):
    def inner(*args, **kwargs):
        print("message")
        return func(*args, **kwargs)
    return inner


@outer
def div_one(a, b):
    return a / b


def div_two(a, b):
    return a / b



if __name__ == "__main__":
    print(div_one(1, 2))
    print("*" * 200)

   
    o = outer(div_two)
    print(o.__name__)
    o(1, 2)
    print("*" * 200)

    print(outer(div_two)(1, 2))
    print("*" * 200)

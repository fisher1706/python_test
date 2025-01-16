class NonIntArgumentException(Exception):
    print("Hello")


def handle_non_arguments(func):
    def wrapper(*args):
        for item in args:
            if item is not int:
                return NonIntArgumentException()
        return func(*args)
    return wrapper


def some_sum_one(a, b, c):
    return a + b + c


@handle_non_arguments
def some_sum_two(a, b, c):
    return a + b + c


if __name__ == '__main__':
    print(some_sum_two(1, 2, 'a'))




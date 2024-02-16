# https://www.youtube.com/watch?v=gfvJj0kFQeg&list=PLlKID9PnOE5h8VJyEiEd_Uv_-tt9KX7MD&index=2


def outer(func):
    def inner(*args, **kwargs):
        print('message')
        return func(*args, **kwargs)
    return inner


def second_outer(*dargs, **dkwargs):
    def outer_two(func):
        def inner_two(*args, **kwargs):
            print(*dargs, **dkwargs)
            return func(*args, **kwargs)
        return inner_two
    return outer_two


@outer
def div(a, b):
    return a / b


@second_outer('mess')
def div_two(a, b):
    return a / b


if __name__ == '__main__':
    print(div(1, 2))
    print(div_two(1, 2))

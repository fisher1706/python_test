# https://www.youtube.com/watch?v=GhgmInoT54c&list=PLlKID9PnOE5h8VJyEiEd_Uv_-tt9KX7MD&index=1

def outer():
    def new_div(a, b):
        return a / b
    var = new_div
    return var


def outer_two():
    def new_div(a, b):
        return a / b
    return new_div


def outer_three(func):
    return func


def outer_four(func):
    def inner(*args, **kwargs):
        print('message')
        return func(*args, **kwargs)
    return inner


def div(a, b):
    return a / b







if __name__ == '__main__':
    my_var = div
    print(type(my_var))
    print(my_var(1, 2))
    print('*' * 200)

    var_1 = outer()
    print(type(var_1))
    print(var_1(1, 2))
    print('*' * 200)

    var_2 = outer_two()
    print(type(var_2))
    print(var_2(1, 2))
    print('*' * 200)

    var_3 = outer_three(div)
    print(type(var_3))
    print(var_3(1, 2))
    print('*' * 200)

    var_4 = outer_four(div)
    print(type(var_4))
    print(var_4(1, 2))
    print('*' * 200)

"""
*args - принимает неограниченное количество позиционных аргументов функции
*kwargs - принимает неограниченное количество аргументов переданных при помощи ключевых слов -> ключ - значение
"""


def my_func_args(a, b, *args):
    print("locals: ", locals())
    print(a, b, args)


def my_func_kwargs(a, b, **kwargs):
    print("locals: ", locals())
    print(a, b, kwargs)

    # for arg in kwargs:
    #     print(arg, kwargs[arg])
    out = [str(arg) + "=" + str(kwargs[arg]) for arg in kwargs]
    print(out)


if __name__ == "__main__":
    my_func_args(1, 2, 2, 4, 5)
    my_func_kwargs(1, 2, x=3, y=4, z=5)

# https://ru.hexlet.io/courses/python-functions/lessons/map-filter-reduce/theory_unit

from functools import reduce

"""
Рассмотрим реализацию функции reduce:

def reduce(func, iterable, initial):
    result = initial
    for item in iterable:
        result = func(result, item)
    return result
В данном примере на вход функции reduce передаются три аргумента:

func — функция, которую мы будем применять к элементам iterable
iterable — итерируемый объект, элементы которого мы будем обрабатывать функцией func
initial — начальное значение, которое будет использоваться при первом вызове функции func

Внутри функции создаем переменную result, которой в качестве начального значения передаем значение initial. 
Затем циклом for проходим по всем элементам объекта iterable и каждый элемент вместе со значением result передаем в 
функцию func. Результат функции func записываем в переменную result. Результатом работы функции reduce будет 
финальное значение переменной result.
"""


def add(x, y):
    return x + y


def multiply(x, y):
    return x * y


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]

    result_add = reduce(add, numbers, 0)
    print(result_add)
    print("*" * 20)

    result_multiply = reduce(multiply, numbers, 1)
    print(result_multiply)

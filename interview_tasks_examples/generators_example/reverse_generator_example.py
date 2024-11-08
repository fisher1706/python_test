"""
Можно перевернуть генератор в Python, используя функцию reversed(). Вот пример, который демонстрирует это:
"""


def func_one(data: list) -> None:
    my_generator = (x**2 for x in data)
    for item in reversed(list(my_generator)):
        print(item)


"""
В этом примере мы используем функцию reversed() вместе с функцией list(), чтобы создать обратный список элементов, 
сгенерированных генератором. Затем мы используем этот список с циклом for для перебора элементов в обратном порядке. 
Если вы работаете с большими наборами данных, может быть полезно использовать обратное итерирование без использования 
list(), чтобы избежать создания полной копии.

Вот пример, который демонстрирует это:
"""


def func_two(data: list) -> None:
    my_generator = (x**2 for x in data)
    for item in reversed(tuple(my_generator)):
        print(item)


"""
Здесь мы используем функцию reversed() вместе с функцией tuple() для обратного итерирования 
через генератор без создания полной копии.
"""


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]

    func_one(my_list)
    print("*" * 200)
    func_two(my_list)

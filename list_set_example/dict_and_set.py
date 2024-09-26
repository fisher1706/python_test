from timeit import timeit
from terminaltables import AsciiTable


"""
dict - словарь, отображение, хеш-мап, ассоциативный массив, коллекция пар ключ - значение,
где ключом может быть только hashable тип, доступ по ключу и проверка наличия ключа 0(1),
начиная с python 3.7 словарь хранит порядок вставки,
пустой словарь лучше создавать через {}, а не через dict(), 
по умолчанию - сразу создается 8 элементов


set - множество, хешсет, неупорядочный набор hashable объектов, доступ и проверка наличия 0(1)


Hashable != Immutable

tuple() - можно положить в set() или использовать как ключ словаря - только если он содержит хешируемые элементы 

set() - нельзя положить в другой set()

a_set = {}
a_list = []
b_set = {a_set} - выдаст ошибку
c_set = {a_list} - выдаст ошибку
print([] in a_set) - выдаст ошибку

при проверке вхождения элемента - попытка получить хеш
"""

x = timeit("dict()")
y = timeit("{}")  # быстрее создает словарь


a_dict = {"x": 1, "y": 2, "z": 3}  # начиная с python 3.7 словарь хранит порядок вставки
a_set = set("xyzx")


b_list = list(range(10000))
b_set = set(b_list)
b_dict = {e: None for e in b_list}


c_list = [["        "] * 8]
c_list[0][3] = '("a", 1)'


class Cat:
    pass


tom = Cat()


class Dog:
    __hash__ = None


a_tuple = (1, 2, 3)  # можно положить в set()
b_tuple = (1, 2, 3, [])  # нельзя положить в set()
d_set = set(a_tuple)


if __name__ == "__main__":
    print(x)
    print(y)
    print("*" * 200)

    print(a_dict)
    print(a_set)
    print("*" * 200)

    in_list = timeit("5_000 in b_list", "from __main__ import b_list", number=100)
    print(in_list)

    in_set = timeit("5_000 in b_set", "from __main__ import b_set", number=100)
    print(in_set)

    in_dict = timeit("5_000 in b_dict", "from __main__ import b_dict", number=100)
    print(in_dict)

    print(in_list < in_set)
    print("*" * 200)

    in_dict_one = timeit("5_000 in a_dict", "from __main__ import a_dict", number=100)
    print(in_dict_one)

    in_dict_two = timeit("9999 in a_dict", "from __main__ import a_dict", number=100)
    print(in_dict_two)

    in_dict_three = timeit(
        "50_000 in a_dict", "from __main__ import a_dict", number=100
    )
    print(in_dict_three)
    print("*" * 200)

    print(c_list)
    print(AsciiTable(c_list).table)
    print("*" * 200)

    print(hash(tom))
    print(id(tom))
    print(id(tom) // 16)
    # print(hash(Dog()))
    print("*" * 200)

    print(d_set)

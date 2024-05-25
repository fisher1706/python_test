"""
Функция all возвращает True, если все элементы истинные (или объект пустой).
"""

first_tuple = (1, 2, 3, 4, 5)
second_tuple = (2, 4, 5)
some_list = [2, 4, 5]


if __name__ == "__main__":
    contains_all = all(elem in first_tuple for elem in second_tuple)
    print(contains_all)

    contains_all = set(some_list).issubset(set(first_tuple))
    print(contains_all)

    print(all(some_list))

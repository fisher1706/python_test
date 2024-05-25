"""
Итераторы поддерживает функцию _next_ для перехода к след элементу return

Генераторы это итератор, элементы которого можно обойти только один раз, элементы не хранятся в памяти, а формируются
на лету. Избегаем memory-error при работе с большими данными.

yield - замораживает итерацию и при повторном вызове
функции продолжается не с начала, а с замороженного значения

Итерируемые типы данных представляют собой объекты, которые могут быть перебраны поэлементно с использованием
цикла или функции, такой как for или while. Это включает в себя типы данных, которые содержат последовательности
элементов, такие как списки, строки, кортежи, множества и словари, а также другие объекты,
которые реализуют протокол итератора.

Вот основные характеристики итерируемых типов данных:

1️⃣ Поддержка итерации: Предоставляют возможность перебора элементов с использованием циклов или функций итерации,
таких как for и while.

2️⃣ Использование встроенной функции iter(): Функция iter() может быть использована для создания итератора из
итерируемого объекта. Он предоставляет метод next(), который возвращает следующий элемент
из итерируемого объекта по требованию.

3️⃣ Использование встроенной функции: while. Э Функция next() может быть использована для получения следующего
элемента из итератора. Когда все элементы итерируемого объекта были извлечены, вызывается исключение StopIteration.

4️⃣ Поддержка для циклов for: Такие объекты могут быть использованы в цикле for для последовательного перебора элементов.

5️⃣ Использование встроенных методов: Также предоставляют встроенные методы для работы с элементами, такие как методы
списков (append(), extend(), remove(), и т. д.).

Итерируемые типы данных являются фундаментальными для работы с коллекциями элементов и широко используются в различных
аспектах программирования, включая обработку данных, манипулирование строками, работу с файлами,
а также в различных структурах данных и алгоритмах.
"""

my_list = [1, 2, 3, 4, 5]
my_iterator_one = iter(my_list)


def my_generator():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5


my_iterator_two = my_generator()


class MyIterator:
    def __init__(self, data):
        self.index = 0
        self.data = data

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        result = self.data[self.index]
        self.index += 1
        return result


if __name__ == "__main__":
    print(next(my_iterator_one))
    print(next(my_iterator_one))
    print(next(my_iterator_one))
    print("*" * 300)

    print(next(my_iterator_two))
    print(next(my_iterator_two))
    print(next(my_iterator_two))
    print("*" * 300)

    i = MyIterator([2, 2, 3])
    print(i.__dict__)

    for val in i:
        print(val)

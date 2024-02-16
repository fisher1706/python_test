"""
Что такое метаклассы
Метакласс это «штука», которая создаёт классы.
Мы создаём класс для того, чтобы создавать объекты, так? А классы являются объектами.
Метакласс это то, что создаёт эти самые объекты.
Что такое type. Как работает поиск метакласса при создании объекта
type это метакласс, который Питон внутренне использует для создания всех классов.

__prepare__ - подготавливает данные - отправляет в __new__
__new__ - создает - чаще всего переопределяется
__init__ - инициализирует
__call__ - при вызове
"""


class Meta(type):
    def __init__(cls, name, base, attrs):
        super().__init__(name, base, attrs)
        cls.MAX_COORD = 100
        cls.MIN_COORD = 0


class Point(metaclass=Meta):
    @staticmethod
    def get_coords():
        return 0, 0


if __name__ == '__main__':
    pt = Point()

    print(pt.MAX_COORD)
    print(pt.get_coords())

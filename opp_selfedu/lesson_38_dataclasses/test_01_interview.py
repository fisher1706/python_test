# https://habr.com/ru/articles/415829/

"""
Одна из новых возможностей, появившихся в Python 3.7 — классы данных (Data classes). Они призваны автоматизировать
генерацию кода классов, которые используются для хранения данных. Не смотря на то, что они используют другие механизмы
работы, их можно сравнить с "изменяемыми именованными кортежами со значениями по умолчанию".

Важно отметить, что аннотации типов обязательны. Все поля, которые не имеют отметок о типе будут проигнорированы.
Конечно, если вы не хотите использовать конкретный тип, вы можете указать Any из модуля typing.
Что же вы получаете в результате? Вы автоматически получаете класс, с реализованными методами
__init__, __repr__, __str__ и __eq__. Кроме того, это будет обычный класс и вы можете наследоваться от него или
добавлять произвольные методы.
"""


from dataclasses import dataclass, field


class Thing:
    def __init__(self, name, weight, price, dims=[]):
        self.name = name
        self.weight = weight
        self.price = price
        self.dims = dims

    def __repr__(self):
        return f"Thing: {self.__dict__}"


@dataclass
class ThingData:
    name: str
    weight: int
    price: float = 0
    dims: list = field(default_factory=list)

    def __eq__(self, other):
        return self.weight == other.weight


"""
__init()__, __repr__, __eq__
"""

if __name__ == '__main__':
    t_1 = Thing("interview_questions", 100, 1024)
    print(t_1)

    t_1.dims.append(10)
    print(t_1)
    print("*" * 200)

    t_2 = Thing("interview_questions", 100, 1024)
    print(t_2)
    print("*" * 200)

    td_1 = ThingData("interview_questions", 100, 1024)
    print(td_1)

    td_2 = ThingData("interview_questions", 100, 1024)
    print(td_1 == td_2)
    print("*" * 200)

    td_2.dims.append(10)

    td_3 = ThingData("zapel", 1000)
    print(td_3.__dict__)


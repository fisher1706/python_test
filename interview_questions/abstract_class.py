"""
Иногда, при создании иерархии классов, необходимо чтобы ряд классов поддерживал одинаковый интерфейс,
например, одинаковый набор методов. Частично эту задачу можно решить с помощью наследования,
однако далеко не всегда дочерним классам подойдет реализация метода из родительского класса.
Абстрактный класс - это класс в котором созданы абстрактные методы - методы, которые обязательно должны
присутствовать в дочерних классах. Создавать экземпляр абстрактного класса нельзя,
его надо наследовать и уже у дочернего класса можно создать экземпляр.
При этом экземпляр дочернего класса можно создать только в том случае,
если у дочернего класса есть реализация всех абстрактных методов.

from abc import ABCMeta - используем для создания абстрактного метакласса
"""


import abc


class Parent(abc.ABC):
    @abc.abstractmethod
    def get_info(self, parameter):
        """Get parameter info"""

    @abc.abstractmethod
    def set_info(self, parameter, value):
        """Set parameter to value"""


class Child(Parent):
    def __init__(self):
        self._parameters = {}

    def get_info(self, parameter):
        return self._parameters.get(parameter)

    def set_info(self, parameter, value):
        self._parameters[parameter] = value
        return self._parameters


if __name__ == '__main__':
    ch = Child()
    print(ch.__dict__)

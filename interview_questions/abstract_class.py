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

Абстрактные классы - это классы содержащие один или несколько абстрактных методов. Абстрактный метод - это метод,
который определен в абстрактном классе, но не имеет реализации в самом классе. Вместо этого они должны быть реализованы
в подклассах, наследующих абстрактный класс.

Основная цель абстрактных классов - предоставить общий интерфейс для всех подклассов, гарантируя, что каждый подкласс
реализует определенный набор методов. Это способствует согласованности и структурности кода,
а также облегчает поддержку и понимание проекта.
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


class Shop(abc.ABC):
    @abc.abstractmethod
    def calc_revenue(self):
        pass


class ClothesShop(Shop):
    def calc_revenue(self):
        return self.shell_count * 5


if __name__ == "__main__":
    ch = Child()
    print(ch.__dict__)

    ch.set_info("name", "Oleg")
    print(ch.__dict__)

    cs = ClothesShop()
    cs.shell_count = 20
    print(cs.__dict__)
    d = cs.calc_revenue()
    print(d)

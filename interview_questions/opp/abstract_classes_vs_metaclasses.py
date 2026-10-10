"""
Разница между абстрактными классами и метаклассами в Python
"""

from abc import ABC, abstractmethod

# --------------------------------------------------
# Абстрактные классы
# --------------------------------------------------


class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return "Woof"


dog = Dog()
print(dog.speak())

# Animal()  # TypeError


# --------------------------------------------------
# Метаклассы
# --------------------------------------------------

class MyMeta(type):
    def __new__(cls, name, bases, attrs):
        print(f"Создаем класс {name}")
        return super().__new__(cls, name, bases, attrs)


class User(metaclass=MyMeta):
    pass


# --------------------------------------------------
# Еще пример метакласса
# --------------------------------------------------

class RequireVersion(type):
    def __new__(cls, name, bases, attrs):
        if "VERSION" not in attrs:
            raise TypeError(f"{name} должен определить VERSION")
        return super().__new__(cls, name, bases, attrs)


class API(metaclass=RequireVersion):
    VERSION = "1.0"


"""
Краткое резюме

Абстрактный класс:
- определяет интерфейс;
- запрещает создание экземпляров, если обязательные методы не реализованы.

Метакласс:
- управляет созданием самих классов;
- позволяет проверять и изменять класс во время его создания.

Иерархия:
метакласс -> класс -> объект

ABC использует метакласс ABCMeta.
"""

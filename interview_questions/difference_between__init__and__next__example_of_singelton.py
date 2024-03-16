"""
Различие между __init__() и __new__() заключается в их роли при создании экземпляров классов.
__init__() – это инициализатор класса. Он вызывается, когда экземпляр класса уже создан, чтобы инициализировать его
начальное состояние. Метод __init__() не возвращает ничего и используется для установки значений атрибутов объекта.

__new__() – это конструктор класса. Он фактически создаёт экземпляр класса и вызывается перед __init__().
Это статический метод, который должен возвращать новый созданный объект, и он используется в особых случаях, например,
при создании экземпляров синглтонов или при наследовании от неизменяемых типов данных, как tuple.

Пример с __init__()
Допустим, у нас есть класс Person, представляющий информацию о человеке.
Мы используем __init__() для инициализации атрибутов каждого объекта этого класса.
В этом примере __init__() используется для установки имени и возраста для каждого объекта Person.
Это самый распространенный способ инициализации атрибутов в объектно-ориентированном программировании.
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


"""
Пример с __new__()
__new__() используется реже, но его можно применять в специфических сценариях, 
например, для создания синглтонов (одиночек).
Здесь __new__() гарантирует, что класс Singleton создает только один экземпляр. 
При попытке создать новый объект этого класса, new() возвращает уже существующий экземпляр, 
если он есть, предотвращая создание новых экземпляров.
"""


class Singleton:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance


if __name__ == '__main__':
    # Создание экземпляра класса Person
    person1 = Person("Алексей", 30)
    print(f"Имя: {person1.name}, Возраст: {person1.age}")
    print("*" * 200)

    # Создание экземпляров Singleton
    singleton1 = Singleton()
    singleton2 = Singleton()

    print(singleton1 is singleton2)  # Вернет True, так как оба объекта являются одним и тем же экземпляром
    print(id(singleton1))
    print(id(singleton2))

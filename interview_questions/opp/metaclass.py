"""
Метаклассы - это концепция, которая позволяет контролировать создание классов.
Классы являются объектами, и они создаются с помощью других классов, которые называются метаклассами.
Вот некоторые ключевые моменты о них:

1️⃣ Классы как объекты: Классы являются объектами первого класса, что означает, что они могут быть созданы,
изменены и переданы как аргументы функций.

2️⃣ Типы и метаклассы: Каждый объект имеет тип, который определяется его классом.
Этот класс, определяющий тип объекта, называется метаклассом. По умолчанию для всех классов метаклассом является type.

3️⃣ Использование метаклассов: Метаклассы можно использовать для изменения поведения создания классов.
Это может быть полезно для автоматического добавления методов, проверки атрибутов или изменения наследования классов.

4️⃣ Ключевые методы метакласса:
Для создания собственного метакласса обычно определяются методы __new__() и __init__().

Метод __new__() вызывается перед созданием экземпляра класса,

а метод __init__() вызывается после создания экземпляра.
"""


class MyMeta(type):
    def __new__(cls, name, bases, dct):
        dct["my_attribute"] = 42
        return super().__new__(cls, name, bases, dct)


class MyClass(metaclass=MyMeta):
    pass


if __name__ == "__main__":
    m = MyClass()
    print(m.__dict__)
    print(m.my_attribute)
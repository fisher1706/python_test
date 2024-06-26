"""
Метод super() используется для обращения к методам и атрибутам родительского класса в подклассе.
Он позволяет вызывать методы родительского класса без явного указания имени этого класса, что делает код более гибким
и поддерживаемым. Вот несколько основных причин, почему этот метод полезен:

1️⃣ Избегание дублирования кода: Позволяет вызывать методы родительского класса, не повторяя их реализацию в подклассе.
Это делает код более читаемым и облегчает его обслуживание, так как логика родительского класса остается в одном месте.

2️⃣ Поддержка множественного наследования: Если ваш класс наследует методы от нескольких родительских классов,
метод super() позволяет вызывать методы родительских классов в порядке, определенном методом разрешения,
что помогает избежать конфликтов и путаницы.

3️⃣ Изменение порядка вызова: Если в будущем вам нужно изменить порядок вызова методов в цепочке наследования,
вам придется изменить всего одну строку в методе, а не каждый вызов метода родительского класса в подклассе.

4️⃣ Улучшение читаемости кода: Использование этого метода делает ваш код более явным и понятным, так как он явно
показывает, что вы вызываете метод родительского класса, а не какой-то другой метод.

"""


class A:
    def __init__(self, param):
        self.URL = 123
        self.param = param
        print(f"url from class A =: {self.URL}")

    def connect(self):
        print(f"{self.URL}")


class B(A):
    def __init__(self, param):
        super().__init__(param)
        self.URL = "localhost"


class Parent:
    def __init__(self):
        self.parent_attribute = "Parent attribute"


class Child(Parent):
    def __init__(self):
        super().__init__()
        self.child_attribute = "Child attribute"


if __name__ == "__main__":
    b = B(100)
    print(b.__dict__)
    b.connect()
    print("*" * 200)

    # Создаем экземпляр дочернего класса
    child = Child()

    # Выводим значения атрибутов
    print(child.parent_attribute)  # Выведет: Parent attribute
    print(child.child_attribute)  # Выведет: Child attribute

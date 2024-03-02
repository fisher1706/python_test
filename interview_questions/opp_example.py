class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        return "Звуки, которые издает животное"


class Dog(Animal):  # Наследование класса Animal
    def speak(self):  # Переопределение метода speak
        return "Гав"


if __name__ == '__main__':
    # Создание объекта класса Dog
    my_dog = Dog("Бобик", 5)
    print(my_dog.speak())  # Вывод: Гав

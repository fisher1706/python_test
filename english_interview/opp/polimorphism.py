"""
Polymorphism

Polymorphism allows objects of different classes to be treated as objects of a common superclass.
It enables code to work with objects of different types without knowing their specific implementation details.
"""


class Vehicle:
    def print_details(self):
        print("Это родительский метод из класса Vehicle")


class Car(Vehicle):
    def print_details(self):
        print("This is a child method from the class Car")


class Cycle(Vehicle):
    def print_details(self):
        print("This is a child method from the class Cycle")


if __name__ == '__main__':
    data = [Vehicle(), Car(), Cycle()]
    for item in data:
        print(item.print_details())

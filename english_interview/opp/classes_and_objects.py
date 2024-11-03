"""
Class & Object
    What is a class?
        A class in Python is like a blueprint for creating objects. It defines the
        attributes (data) and methods (functions) that the objects created from
        the class will have. In python a class is created by the keyword class.
    What is an object?
        An object is created using the constructor of the class. This object will
        then be called the instance of the class.

Methods:
    Methods are functions defined within a class that operate on the objects of that class.
    They allow objects to perform actions and manipulate their internal state.

Self:
    parameter is a reference to the current instance of the class, and is used to access
    variables that belongs to the class.

Constructor in Python:
    In Python, the constructor method is named init(). It is called automatically when you create a new object from
    a class. You can pass arguments to the constructor to initialize object-specific values.
"""


class Dog:
    # attribute
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    # methods
    def bark(self):
        print(f"{self.name} says: Woof!")


if __name__ == "__main__":
    my_dog = Dog("Buddy", "Labrador")
    my_dog.bark()

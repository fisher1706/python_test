"""
Class and Static Methods
    Class methods operate on the class itself,
    while static methods are utility functions that operate independently of any specific instance or class.

    @classmethod -> change behavior of class

    A static method in Python is a method defined within a class that doesn’t require access to the instance (object)
    or class itself. It behaves like a regular function but belongs to the class’s namespace. You can call it on the
    class itself or on instances of the class, and it doesn’t take self or cls as its first parameter.

    Self keyword is used to refer to the current class object. It is passed as the first argument to class methods
    and allows you to work with the class object's attributes and methods inside those methods.
"""


class Bank:
    general_message = "empty"

    def print_general_message(self):
        print(self.general_message)

    @classmethod
    def change_general_message(cls, new_message):
        cls.general_message = new_message


class Vector:
    MIN_COORD = 0
    MAX_COORD = 100

    @classmethod
    def validate(cls, arg):
        return cls.MIN_COORD <= arg <= cls.MAX_COORD

    @staticmethod
    def norm_two(x, y):
        return x * x + y * y

    def __init__(self, x, y):
        self.x = self.y = 0
        if self.validate(x) and self.validate(y):
            self.x = x
            self.y = y

        print(self.norm_two(x, y))

    def get_coord(self):
        return self.x, self.y


if __name__ == '__main__':
    b1 = Bank()
    b2 = Bank()

    b1.print_general_message()
    b2.print_general_message()
    print("*" * 200)

    b1.change_general_message("new_message")
    b1.print_general_message()
    b2.print_general_message()
    print("*" * 200)

    Bank.print_general_message(b1)
    print("*" * 200)



    v = Vector(1, 2)

    res_one = v.get_coord()
    print(res_one)
    print("*" * 200)

    res_two = Vector.get_coord(v)
    print(res_two)
    print("*" * 200)

    print(Vector.validate(5))
    print(v.validate(3))
    print("*" * 200)

    print(Vector.norm_two(5, 6))
    print(v.norm_two(3, 4))
    print("*" * 200)

"""
Multiple Inheritance
    Python allows a class to inherit from multiple base classes, enabling code reuse and the combination
    of behaviors from different classes.

MRO (Method Resolution Order)
    Is the order in which Python looks for methods and attributes of a class when they are called.
    This order is especially important in the context of multiple inheritance, where a class inherits behavior
    and attributes from several parent classes, and it is necessary to clearly define where exactly to get these
    attributes and methods from when they overlap.

super() Function
    The super() function in Python is used to call parent class methods from a child class.
    This is especially useful in the __init__ constructor when you need to initialize attributes of the base class.
"""


class A:
    pass


class B(A):
    pass


class C(A):
    pass


class D(B, C):
    pass


if __name__ == "__main__":
    print(D.mro())
    print("*" * 300)

    print(D.__mro__)

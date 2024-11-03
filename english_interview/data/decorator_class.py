"""
Class decorators modify classes.
"""


def class_decorator(cls):
    cls.extra_attribute = 'This is an extra attribute'
    return cls


@class_decorator
class MyClass:
    @staticmethod
    def greet():
        return "Hello!"



if __name__ == '__main__':
    obj = MyClass()
    print(obj.extra_attribute) # Output: This is an extra attribute

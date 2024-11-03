"""
Optimize memory usage by limiting class attributes.
"""


class MyClass:
    __slots__ = ['attr1', 'attr2']

    # Only these attributes can be used
    def __init__(self, attr1, attr2):
        self.attr1 = attr1
        self.attr2 = attr2


if __name__ == '__main__':
    obj = MyClass(1, 2)
    print(obj.attr1) # Output: 1
    obj.attr3 = 3 # Raises an AttributeError

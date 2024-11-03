"""
Metaclasses modify class creation.
"""


class Meta(type):
    def __new__(cls, name, bases, attrs):
        attrs['greeting'] = 'Hello'
        return super().__new__(cls, name, bases, attrs)


class MyClass(metaclass=Meta):
    pass


if __name__ == '__main__':
    obj = MyClass()
    print(obj.greeting)
    
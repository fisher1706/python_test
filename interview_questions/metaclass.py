class MyMeta(type):
    def __new__(cls, name, bases, dct):
        dct['my_attribute'] = 42
        return super(MyMeta, cls).__new__(cls, name, bases, dct)


class MyClass(metaclass=MyMeta):
    pass


if __name__ == '__main__':
    m = MyClass()
    print(m.__dict__)
    print(m.my_attribute)

# https://www.youtube.com/watch?v=5WNZf1NRZUw

class B:
    def __set_name__(self, obj, name):
        print(f'__set_name__ {name}')
        self.name = '_' + name

    def __get__(self, obj, objtype=None):
        return getattr(obj, self.name)

    def __set__(self, obj, val):
        if not isinstance(val, int):
            raise ValueError
        print(f'__set__ {self.name} = {val}')
        setattr(obj, self.name, val)


class X:
    a = 1
    b = B()
    # c = B()

    def __getattr__(self, name):
        print(f'__getattr__ {name}')
        return 0

    # def __getattribute__(self, name):
    #     print(f'__getattribute__ {name}')
    #     if len(name) == 1:
    #         return -1
    #     else:
    #         super().__getattribute__(name)

    def __init__(self):
        self.b = 2
        # self.c = 3






x = X()


# print('x.a =', x.a)
# print('x.b =', x.b)
# print('x.c =', x.c)
print('x.__dict__ =', x.__dict__)
# print('X.__dict__ =', X.__dict__)

# x.b = '123'


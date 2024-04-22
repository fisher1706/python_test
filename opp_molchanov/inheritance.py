"""
https://www.patreon.com/oleg_molchanov/posts?filters[tag]=%23%D0%BA%D1%83%D1%80%D1%81%D0%9E%D0%9E%D0%9F
password: xau8ahPh
lesson №13
lesson №14
"""


class IntelCpu:
    cpu_socket = 1151
    name = 'Intel'


class I7(IntelCpu):
    pass


class I5(IntelCpu):
    pass




if __name__ == '__main__':
    x = I5()

    print(x.__dict__)
    print(x.name, x.cpu_socket)

    x.name = '123'
    print(x.__dict__)
    print(type(x))

    i5 = I5()
    i7 = I7()

    a = isinstance(i5, IntelCpu)
    print(a)

    b = type(i5)
    print(b)

    c = issubclass(I5, IntelCpu)
    print(c)

    d = isinstance(i5, type(i7))
    print(d)

    print(issubclass(I5, IntelCpu))


"""
https://www.patreon.com/oleg_molchanov/posts?filters[tag]=%23%D0%BA%D1%83%D1%80%D1%81%D0%9E%D0%9E%D0%9F
password: xau8ahPh
lesson №11
"""


class Person:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        print('From get_name()')
        return self._name

    def set_name(self, value):
        print('From set_name()')
        self._name = value

    # name = property(fget=get_name, fset=set_name)

    name = property()
    print('type name:', type(name))

    name = name.getter(get_name)
    name = name.setter(set_name)


if __name__ == '__main__':
    p = Person('Dima')

    print(p.__dict__)
    print(p.name)

    p.name = 'Oleg'
    print(p.name)


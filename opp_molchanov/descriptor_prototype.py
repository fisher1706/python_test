"""
https://www.patreon.com/oleg_molchanov/posts?filters[tag]=%23%D0%BA%D1%83%D1%80%D1%81%D0%9E%D0%9E%D0%9F
password: xau8ahPh
lesson №18
"""


class StringD:
    def __init__(self, value=None):
        if value:
            self.set(value)

    def set(self, value):
        self._value = value

    def get(self):
        return self._value


class Person:
    def __init__(self, name, surname):
        self.name = StringD(name)
        self.surname = StringD(surname)



if __name__ == '__main__':
    p = Person('Ivan', 'Ivanoff')

    print(p.__dict__)
    print(dir(p))

    print(p.name)
    print(p.name.get())
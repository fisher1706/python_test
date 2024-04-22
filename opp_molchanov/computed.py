"""
https://www.patreon.com/oleg_molchanov/posts?filters[tag]=%23%D0%BA%D1%83%D1%80%D1%81%D0%9E%D0%9E%D0%9F
password: xau8ahPh
lesson №12
"""


class Person:
    def __init__(self, name, surname):
        self._name = name
        self._surname = surname
        self._full_name = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
        self._full_name = None

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, value):
        self._surname = value
        self._full_name = None

    @property
    def full_name(self):
        if self._full_name is None:
            self._full_name = f'{self._name} {self._surname}'
        return self._full_name






if __name__ == '__main__':
    p = Person('oleg', 'zapel')

    x = p.full_name
    print(x)

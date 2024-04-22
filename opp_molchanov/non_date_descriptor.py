"""
https://www.patreon.com/oleg_molchanov/posts?filters[tag]=%23%D0%BA%D1%83%D1%80%D1%81%D0%9E%D0%9E%D0%9F
password: xau8ahPh
lesson №18
"""


from random import choice


class Choise:
    def __init__(self, *choise):
        self._choise = choise

    def __get__(self, obj, owner):

        print(f'Self: {self}')
        print(f'obj: {obj}')
        print(f'owner: {owner}')

        return choice(self._choise)

class Game:
    dice = Choise(1, 2, 3, 4, 5, 6)
    flip = Choise('Heads', 'Tails')


if __name__ == '__main__':
    g = Game()

    x = g.flip
    print(x)

    y = g.dice
    print(y)

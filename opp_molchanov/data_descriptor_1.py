"""
https://www.patreon.com/oleg_molchanov/posts?filters[tag]=%23%D0%BA%D1%83%D1%80%D1%81%D0%9E%D0%9E%D0%9F
password: xau8ahPh
lesson №18
lesson №19
"""


from time import time


class Epoch:
    def __get__(self, instance, owner_class):
        print(f'id of self: {id(self)}')

        print(f'Self: {self}')
        print(f'Instance: {instance}')
        print(f'Owner class: {owner_class}')

        if instance is None:
            return self
        return int(time())

    def __set__(self, instance, value):
        pass


class MyTime:
    epoch = Epoch()


if __name__ == '__main__':
    m1 = MyTime()
    print(m1.epoch)

    m2 = MyTime()
    print(m2.epoch)

    print(MyTime.epoch)











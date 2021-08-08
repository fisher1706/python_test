class Person:
    def __init__(self, name):
        # print('init Person')
        self.name = name

    def breathe(self):
        print('Я могу дышать.')

    def walk(self):
        print('Я могу ходить')

    def sleep(self):
        print('Человек спит')

    def combo(self):
        self.breathe()
        self.walk()
        self.sleep()

    def __str__(self):
        return f'Person {self.name}'

class Doctor(Person):
    def breathe(self):
        print('Доктор дышит.')

    def __str__(self):
        return f'Doctor {self.name}'

d = Doctor('John')
p = Person('Adam')

# d.breathe()
# p.breathe()

# print(d.name, p.name)
# print(d.__dict__)
# print(d.name)

# print(p, d)
# p.combo()
d.combo()




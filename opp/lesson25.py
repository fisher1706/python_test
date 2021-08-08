class Person:
    def can_breathe(self):
        print('Я могу дышать.')

    def can_walk(self):
        print('Я могу ходить')


class Doctor(Person):
    def ca_cure(self):
        print('Я могу лечить.')


class Architech(Person):
    def can_build(self):
        print('Я могу строить.')


# d = Doctor()
# d.ca_cure()
# d.can_breathe()
# d.can_walk()
#
# a = Architech()
# a.can_build()
# a.can_breathe()
# a.can_walk()

print(issubclass(Doctor, Person))
print(issubclass(Person, Doctor))
class Cat:

    def set_value(self, value, age=0):
        self.name = value
        self.age = age

    def __init__(self, name, breed='pers', age=1, color='white'):
        print('hello new object is', self)
        self.name = name
        self.breed = breed
        self.age = age
        self.color = color






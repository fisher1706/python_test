class Temperature:
    def __init__(self, *, celsius=0):
        self.celsius = celsius

    @property
    def fahrenheit(self):
        return self.celsius * 9/5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = (value - 32) * 5/9

    @fahrenheit.deleter
    def fahrenheit(self):
        del self.celsius


c = Temperature()

c.fahrenheit = 451
print(c.celsius)

c.celsius = 100
print(c.fahrenheit)

def a(*args):
    [print(i) for i in args]

if __name__ == '__main__':
    a(4, 5)
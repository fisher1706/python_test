"""
Assuming that rover is an instance of the Dog class, what is an equivalent of this line of code?

rover.speak()

Dog.speak(rover)

"""


class Dog:
    data = "test"

    def speak(self):
        print(self.data)


if __name__ == '__main__':
    rover = Dog()
    rover.speak()

    Dog.speak(rover)
    
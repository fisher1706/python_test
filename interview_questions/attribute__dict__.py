class Person:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print("Hello, my name is", self.name)


if __name__ == "__main__":
    p = Person("Oleg")

    print(p.__dict__)

    p.age = 25
    print(p.__dict__)

    p.__dict__["name"] = "Fisher"
    print(p.__dict__)

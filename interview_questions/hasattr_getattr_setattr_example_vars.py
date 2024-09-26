class Test:
    def __init__(self, name):
        self.name = name

    def method_one(self):
        print(self.name)


if __name__ == "__main__":
    t1 = Test("object_testing")

    print(hasattr(t1, "name"))
    print(hasattr(t1, "test"))
    print(hasattr(t1, "method_one"))

    print(getattr(t1, "name"))
    print(getattr(t1, "method_one"))
    print(getattr(t1, "test", None))

    setattr(t1, "zapel", "fisher")
    print(t1.__dict__)
    print(t1.zapel)

    delattr(t1, "zapel")
    print(t1.__dict__)

    print(vars(Test))
    print(vars(t1))

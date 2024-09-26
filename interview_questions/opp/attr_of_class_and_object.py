class A:
    attr: str = "Zapel"

    def __init__(self, attr: str):
        self.attr = attr


if __name__ == "__main__":
    a = A("Oleg")

    print(a.__dict__)
    print(A.__dict__)

    print(a.attr)

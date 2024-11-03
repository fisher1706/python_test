"""
Composition
    Composition is an alternative to inheritance, where an object contains instances of other objects as attributes,
    allowing for code reuse and flexible object composition.
"""


class Bill:
    def __init__(self, description):
        self.description = description


class Tail:
    def __init__(self, length):
        self.length = length


class Duck:
    def __init__(self, bill: Bill, tail: Tail) -> None:
        self.bill = bill
        self.tail = tail

    def about(self) -> None:
        print("This duck has a", self.bill.description, "bill and a", self.tail.length, "tail")


if __name__ == "__main__":
    t = Tail("long")
    b = Bill("wide orange")
    duck = Duck(b, t)

    duck.about()

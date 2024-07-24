"""
__repr__ - восстанавливает состояние объекта
"""


class Banknote:
    def __init__(self, value: int) -> None:
        self.value = value

    def __repr__(self):
        return f"Banknote({self.value})"

    def __str__(self):
        return f"banknote value: {self.value}"


if __name__ == '__main__':
    b = Banknote(10)

    print(b)
    print(f"{b!r}")

    other = eval(repr(b))
    print(other)

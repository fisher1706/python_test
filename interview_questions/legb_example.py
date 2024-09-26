data = "global"


def outer_one():
    data = "enclosing"

    def inner():
        data = "local"
        print(data)

    inner()


def outer_two():
    data = "enclosing"

    def inner():
        print(data)

    inner()


def outer_three():
    def inner():
        print(data)

    inner()


if __name__ == "__main__":
    outer_one()
    outer_two()
    outer_three()

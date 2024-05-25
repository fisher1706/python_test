class MyClass:
    """This is the docstring for MyClass."""

    attribute_name = "value"


if __name__ == "__main__":
    print(MyClass.__doc__)
    print("*" * 300)
    help(MyClass)

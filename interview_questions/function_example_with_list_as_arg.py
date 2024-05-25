def some_function(some_arg: list = []):
    print(id(some_arg))
    some_arg.append(1)
    return some_arg


if __name__ == "__main__":
    print(some_function())
    print(some_function())
    print(some_function())

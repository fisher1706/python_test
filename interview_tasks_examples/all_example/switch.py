def numbers_to_strings(argument):
    switcher = {
        0: "zero",
        1: "one",
        2: "two",
    }

    return switcher.get(argument, "nothing")


if __name__ == "__main__":
    arg = 0
    print(numbers_to_strings(arg))

    arg = 4
    print(numbers_to_strings(arg))

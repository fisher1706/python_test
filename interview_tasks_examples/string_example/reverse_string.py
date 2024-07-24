string = "this is a string"


def reverse(str_out):
    if len(str_out) <= 1:
        return str_out
    return str_out[::-1]


if __name__ == "__main__":
    print(string[::-1])

    str2 = "hello"

    print(reverse(str2))

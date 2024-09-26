a = ["hello", "world"]
b = ("hello", "world")


if __name__ == "__main__":
    print(id(a[0]), id(b[0]))

    x = a[0].replace("o", "GG")
    print(x)
    print(id(x), id(a[0]))

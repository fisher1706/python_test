text = "123"


if __name__ == '__main__':
    print(dir(text))
    print([e for e in dir(text) if e.startswith("_")])

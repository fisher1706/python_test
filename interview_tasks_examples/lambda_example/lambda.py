some_list = [1, 2, 3, "a"]


if __name__ == "__main__":
    print(list(filter(lambda x: isinstance(x, int), some_list)))

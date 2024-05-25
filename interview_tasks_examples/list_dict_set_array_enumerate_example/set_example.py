list_one = [1, 2, 3, 4]
list_two = [1, 3]


if __name__ == "__main__":
    c = list(set(list_one) - set(list_two))
    print(c)

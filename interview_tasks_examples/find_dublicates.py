"""
find dublicates
"""


def get_dublicates(example_list):
    new_list = list()
    dublicate = list()
    for el in example_list:
        if el in new_list:
            dublicate.append(el)
        else:
            new_list.append(el)
    return "not found" if len(dublicate) == 0 else new_list, dublicate


"""
check dublicates
"""


def check_dublicates(example_list):
    return len(example_list) != len(set(example_list))


if __name__ == '__main__':
    example_one = [1, 1, 1, 4, 2, 5]
    n, d = get_dublicates(example_one)
    print(n, d)
    print("*" * 200)

    example_two = [1, 4, 2, 5]
    n, d = get_dublicates(example_two)
    print(n, d)
    print("*" * 200)

    check = check_dublicates(example_one)
    print(check)
    print("*" * 200)

    check = check_dublicates(example_two)
    print(check)
    print("*" * 200)

"""
find duplicates
"""


def get_duplicates(example_list):
    new_list = list()
    duplicates = list()
    for el in example_list:
        if el in new_list:
            duplicates.append(el)
        else:
            new_list.append(el)
    return "not found" if len(duplicates) == 0 else new_list, duplicates


"""
check dublicates
"""


def check_duplicates(example_list):
    return len(example_list) != len(set(example_list))


if __name__ == '__main__':
    example_one = [1, 1, 1, 4, 2, 5]
    n, d = get_duplicates(example_one)
    print(n, d)
    print("*" * 200)

    example_two = [1, 4, 2, 5]
    n, d = get_duplicates(example_two)
    print(n, d)
    print("*" * 200)

    check = check_duplicates(example_one)
    print(check)
    print("*" * 200)

    check = check_duplicates(example_two)
    print(check)
    print("*" * 200)

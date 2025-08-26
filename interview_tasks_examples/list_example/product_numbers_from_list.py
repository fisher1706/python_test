from functools import reduce


def extract_number(data):
    if isinstance(data, int):
        return [data]
    if isinstance(data, (list, tuple, set)):
        return [j for j in data if isinstance(j, int)]
    return []


def list_product(data):
    l1 = []
    for i in data:
        if isinstance(i, dict):
            for j in list(i.values()) + list(i.keys()):
                l1.extend(extract_number(j))
        else:
            l1.extend(extract_number(i))

    print(f"l1: {l1}")

    if not l1:
        return None  # or 1, depending on desired behavior

    return reduce(lambda x, y: x * y, l1)



if __name__ == "__main__":
    list1 = [
        1,
        2,
        3,
        4,
        [44, 55, 66, True],
        False,
        (34, 56, 78, 89, 34),
        {1, 2, 3, 3, 2, 1},
        {1: 34, "key2": [55, 67, 78, 89], 4: (45, 22, 61, 34)},
        [56, "data science"],
        "Machine Learning",
    ]

    print("list1 = ", list1)
    print(" ")
    print("Product of Numbers in list1 = ", list_product(list1))

from functools import reduce


def extract_number(data):
    l = []

    if type(data) == int:
        l.append(data)
        return l

    if type(data) == list or type(data) == tuple or type(data) == set:
        for j in data:
            if type(j) == int:
                l.append(j)
        return l


def list_product(l):
    l1 = []
    for i in l:
        if type(i) == dict:
            for j in list(i.values()):
                l1.extend(extract_number(j)) if type(extract_number(j)) == list else None
            for j in list(i.keys()):
                l1.extend(extract_number(j)) if type(extract_number(j)) == list else None
        else:
            l1.extend(extract_number(i)) if type(extract_number(i)) == list else None

    return reduce(lambda x, y: x * y, l1)


if __name__ == '__main__':
    list1 = [
        1, 2, 3, 4,
        [44, 55, 66, True],
        False,
        (34, 56, 78, 89, 34),
        {1, 2, 3, 3, 2, 1},
        {1: 34, "key2": [55, 67, 78, 89], 4: (45, 22, 61, 34)},
        [56, 'data science'],
        'Machine Learning'
    ]

    print("list1 = ", list1)
    print(" ")
    print("Product of Numbers in list1 = ", list_product(list1))

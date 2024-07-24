def extract_number(data):
    out = []
    for val in data:
        if isinstance(val, int) and not isinstance(val, bool):
            out.append(val)
        if isinstance(val, (list, tuple, set)):
            for j in val:
                if isinstance(j, int) and not isinstance(j, bool):
                    out.append(j)
        if isinstance(val, dict):
            for k in val.keys():
                if isinstance(k, int) and not isinstance(k, bool):
                    out.append(k)
            for v in val.values():
                if isinstance(v, int) and not isinstance(v, bool):
                    out.append(v)
    return sum(out)


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

    x = extract_number(list1)
    print(x)

    i = False
    print(isinstance(i, int))

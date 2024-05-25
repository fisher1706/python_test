def count_list(data):
    dct = {}
    for el in data:
        dct[el] = data.count(el)
    return dct


def count_list_of_tuple(data):
    out = []

    index = [0, len(data)]
    for i in range(1, len(data)):
        if data[i - 1] != data[i]:
            index.append(i)
    index.sort()

    for i in range(1, len(index)):
        out.append((data[index[i - 1]], len(data[index[i - 1] : index[i]])))
    return out


def sorted_list_of_lists(data, index):
    return sorted(data, key=lambda x: x[index])


if __name__ == "__main__":
    txt = "aaaagggggvvvvvcaaaah"
    sort_txt = count_list_of_tuple(txt)
    print(sort_txt)

    start_data = [[0, 1, "f"], [4, 2, "t"], [9, 4, "afsd"]]

    sort_data = sorted_list_of_lists(start_data, 1)
    print(sort_data)

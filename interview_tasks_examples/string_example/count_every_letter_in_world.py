def count_symbols_in_string(data: str) -> dict:
    dct = {}
    for el in data:
        dct[el] = data.count(el)
    return dct


def separate_string_on_list_of_tuple(data: str) -> list[tuple]:
    out = []

    index = [0, len(data)]
    for i in range(1, len(data)):
        if data[i - 1] != data[i]:
            index.append(i)
    index.sort()

    for i in range(1, len(index)):
        out.append((data[index[i - 1]], len(data[index[i - 1]: index[i]])))
    return out


if __name__ == "__main__":
    txt = "aaaagggggvvvvvcaaaah"

    out_one = count_symbols_in_string(txt)
    print(out_one)

    sort_txt = separate_string_on_list_of_tuple(txt)
    print(sort_txt)

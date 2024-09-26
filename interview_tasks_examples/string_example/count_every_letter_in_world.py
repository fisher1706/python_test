def count_symbols_in_string(data: str) -> dict:
    dct = {}
    for el in data:
        dct[el] = data.count(el)
    return dct


def separate_string_on_list_of_tuple(data: str) -> list[tuple]:
    out = []
    index = [0]  # Start with the first index

    # Find indices where the character changes
    for i in range(1, len(data)):
        if data[i] != data[i - 1]:
            index.append(i)
    index.append(len(data))  # Append the last index

    # Create tuples of (character, length of consecutive sequence)
    for i in range(1, len(index)):
        char = data[index[i - 1]]
        length = index[i] - index[i - 1]
        out.append((char, length))

    return out


if __name__ == "__main__":
    txt = "aaaagggggvvvvvcaaaah"

    out_one = count_symbols_in_string(txt)
    print(out_one)

    sort_txt = separate_string_on_list_of_tuple(txt)
    print(sort_txt)

from itertools import zip_longest


def merge_lists_to_tuples(data1, data2, fill_value=None):
    merged_list = [(a, b) for a, b in zip_longest(data1, data2, fillvalue=fill_value)]
    print("merged_list", merged_list)
    out_without_none = [i for value in merged_list for i in value if i]
    out_with_none = [i for value in merged_list for i in value]
    return out_without_none, out_with_none


if __name__ == "__main__":
    list1 = [1, 2, 3]
    list2 = [4, 5, 6, 7, 8]

    x, y = merge_lists_to_tuples(list1, list2)
    print(x)
    print(y)

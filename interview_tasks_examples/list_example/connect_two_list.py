from itertools import zip_longest


def merge_lists_to_tuples(data1, data2, fillvalue=None):
    merged_list = [(a, b) for a, b in zip_longest(data1, data2, fillvalue=fillvalue)]
    out = [i for value in merged_list for i in value]
    return out


if __name__ == '__main__':
    list1 = [1, 2, 3]
    list2 = [4, 5, 6, 7, 8]

    x = merge_lists_to_tuples(list1, list2)
    print(x)

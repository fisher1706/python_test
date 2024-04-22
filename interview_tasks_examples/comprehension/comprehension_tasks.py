def change_dict(data):
    out = {key: sum(val) for key, val in data.items()}
    print(out)


def convert_to_list(data):
    out = [i for val in data.values() for i in val]
    print(out)


if __name__ == '__main__':
    my_dict = {"key1": [1, 2, 3, 4],
               "key2": [5, 6, 7, 8],
               "key3": [9, 10, 11, 12]
               }

    change_dict(my_dict)
    convert_to_list(my_dict)

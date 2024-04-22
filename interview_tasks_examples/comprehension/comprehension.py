def dict_comprehension(data):
    dict_comp = {key: val for key, val in enumerate(data)}
    print(dict_comp)


def list_comprehension(data):
    list_comp = [i for i in range(len(data))]
    print(list_comp)


if __name__ == '__main__':
    sample = ['one', 'two', 'three']

    dict_comprehension(sample)
    list_comprehension(sample)

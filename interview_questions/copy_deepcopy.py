import copy


my_list = [1, 2, 3]

new_list = my_list.copy()
deep_new_list = copy.deepcopy(my_list)


if __name__ == '__main__':
    print(id(my_list))
    print(id(new_list))
    print(id(deep_new_list))

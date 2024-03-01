import copy


my_list = [1, 2, 3, [1, 2]]

new_list = my_list.copy()
deep_new_list = copy.deepcopy(my_list)


if __name__ == '__main__':
    print(f"id_my_list: = {id(my_list)}")
    print(f"id_el_my_list:= {id(my_list[3])}")

    print(f"id_new_list: = {id(new_list)}")
    print(f"id_el_new_list:= {id(new_list[3])}")

    print(f"id_deep_new_list: = {id(deep_new_list)}")
    print(f"id_deep_new_list:= {id(deep_new_list[3])}")

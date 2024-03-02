def change_data_list(my_list: list) -> list:
    out_list = []
    for val in my_list:
        if val % 15 == 0:
            out_list.append("FizBuz")
        elif val % 5 == 0:
            out_list.append("Fiz")
        elif val % 3 == 0:
            out_list.append("Buz")
        else:
            out_list.append(val)
    return out_list


if __name__ == '__main__':
    old_list = [15, 7, 8, 5, 3, 1]
    data = change_data_list(old_list)
    print(data)

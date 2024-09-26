# https://www.youtube.com/watch?v=yEAI3CC_sBE&list=PLhqLR-FtmNaXXnYQ7tsy2Fw7USL14fdfB&index=3


def del_elements_from_list_by_number(list_to_del: list, number: int) -> list:
    out = [el for i, el in enumerate(list_to_del) if (i + 1) % number != 0]
    return out


# do not work
def del_elements_from_list_by_number_by_slice(list_to_del: list, number: int) -> list:
    print(list[number::number])
    del list_to_del[number::number]
    return list_to_del


if __name__ == "__main__":
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    x = del_elements_from_list_by_number(data, 4)
    print(x)

    x = del_elements_from_list_by_number_by_slice(data, 4)
    print(x)

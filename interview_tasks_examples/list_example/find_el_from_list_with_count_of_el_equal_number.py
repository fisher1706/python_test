def find_el_from_list_with_count_of_el_equal_number(my_list: list, number: int = 1) -> dict:
    out = {el: my_list.count(el) for el in my_list if my_list.count(el) == number}
    return out


if __name__ == "__main__":
    data = [1, 2, 3, 4, 5, 2, 1, 3, 4]

    x = find_el_from_list_with_count_of_el_equal_number(data)
    print(x)

    x = find_el_from_list_with_count_of_el_equal_number(data, number=2)
    print(x)

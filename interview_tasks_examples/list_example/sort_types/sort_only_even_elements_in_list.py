def sort_even_elements_in_list(input_list: list) -> list:
    odds = sorted((x for x in input_list if x % 2 == 0), reverse=True)
    out = [x if x % 2 != 0 else odds.pop() for x in input_list]
    return out


if __name__ == '__main__':
    data = [1, 2, 3, 14, 18, 22, 4, 5, 6, 7, 8, 9, 10]

    y = sort_even_elements_in_list(data)
    print(y)

def find_pairs(my_list, number):
    pairs = []
    for i, el_1 in enumerate(my_list):
        for j, el_2 in enumerate(my_list[i + 1 :]):
            if el_1 + el_2 == number:
                pairs.append((el_1, el_2))
    return pairs


if __name__ == "__main__":
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    n = 5

    print(find_pairs(data, n))

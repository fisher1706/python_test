def sorted_list_of_lists(data: list, index: int) -> list[list]:
    return sorted(data, key=lambda x: x[index])


if __name__ == "__main__":
    start_data = [[0, 1, "f"], [4, 2, "t"], [9, 4, "afsd"]]

    sort_data = sorted_list_of_lists(start_data, 2)
    print(sort_data)

    print(id(start_data))
    print(id(sort_data))

def replace_elements_of_list(data: list) -> None:
    for i in range(len(data) // 2):
        data[i], data[len(data) - i - 1] = data[len(data) - i - 1], data[i]
    print(data)


if __name__ == "__main__":
    A2 = [1, 2, 3, 4, 5]

    replace_elements_of_list(A2)

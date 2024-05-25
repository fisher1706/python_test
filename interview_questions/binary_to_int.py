binary_str = "110101"


def func_one(string=binary_str):
    decimal_num = int(string, 2)
    print(decimal_num)


def func_two(string=binary_str):
    decimal_num = 0
    for i in range(len(binary_str)):
        decimal_num += int(string[i]) * 2 ** (len(string) - i - 1)
    print(decimal_num)


if __name__ == "__main__":
    func_one()
    func_two()

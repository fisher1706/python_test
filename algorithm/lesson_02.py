def func_one(data: int) -> bool:
    flag = False
    for i in range(data):
        flag = (i % 10 == 0) or flag
    return flag


def func_two(data: int) -> bool:
    flag = True
    for i in range(data):
        flag = flag and (i % 10 == 0)
    return flag


def func_three(data: int):
    for i in range(data):
        if i % 3 == 0 and i % 2 == 0:
            print(i)
        else:
            print("zapel")


if __name__ == "__main__":
    print(func_one(15))
    print(func_two(15))

    func_three(10)

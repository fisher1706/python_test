def func_one(data):
    out = []

    index = [0, len(data)]
    for i in range(1, len(data)):
        if data[i] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            index.append(i)
    index.sort()

    for i in range(1, len(index)):
        out.append((data[index[i - 1]: index[i]]).lower())

    return tuple(out)


def func_two(data, func=func_one):
    data_inner = data.split(",")
    out = []

    for inner_val in data_inner:
        inner = func(inner_val)
        out.append(inner)

    return tuple(out)


if __name__ == "__main__":
    val = "PythonIsGreat"
    val_big = "PythonIsGreat,LinuxIsAwesome"

    print(func_one(val))
    print(func_two(val_big))

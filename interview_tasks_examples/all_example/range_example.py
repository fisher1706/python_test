def range_example(num: int) -> int:
    out = None
    for i in range(num):
        out = i * 3
    return out


if __name__ == "__main__":
    x = range_example(10)
    print(x)

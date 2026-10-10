def range_example(num: int) -> int:
    out = None
    for i in range(num):
        print(i)
        out = i * 3
        print(out)
    return out


if __name__ == "__main__":
    x = range_example(10)
    print(x)

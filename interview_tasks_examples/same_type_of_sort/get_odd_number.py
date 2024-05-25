def odd(number):
    out = []
    for i in range(1, number):
        if i % 2 != 0:
            out.append(i)
    return out


if __name__ == "__main__":
    x = odd(23)
    print(x)

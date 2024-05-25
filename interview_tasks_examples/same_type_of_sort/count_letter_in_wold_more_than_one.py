def count_symbols(data):
    out = {}
    for el in data:
        if data.count(el) > 1:
            out[el] = data.count(el)
    print(out)
    return "".join(out.keys())


if __name__ == "__main__":
    a = "someteststring"

    x = count_symbols(a)
    print(x)

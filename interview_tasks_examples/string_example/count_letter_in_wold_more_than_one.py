
def count_symbols(data):
    out = {}
    for el in data:
        if data.count(el) > 1:
            out[el] = data.count(el)
    print(out)
    return "-".join(out.keys())


def count_complex_symbols(data):
    return {el: data.count(el) for el in data if data.count(el) > 1}


if __name__ == "__main__":
    a = "someteststring"

    x = count_symbols(a)
    print(x)

    y = count_complex_symbols(a)
    print(y)

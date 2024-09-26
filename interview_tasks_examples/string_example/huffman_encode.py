# https://www.youtube.com/watch?v=40BLw-4aK0o

from collections import Counter


def count_of_letters(string):
    inner = [(freq, ch) for ch, freq in Counter(string).items()]
    x = sorted(inner)
    return x


def make_tree(text):
    num = None
    se = set(text)
    ls = [(text.count(ch), ch) for ch in se]
    ls.sort()

    while len(ls) >= 2:
        d = (ls[0][0] + ls[1][0], (ls[0][1], ls[1][1]))
        # print(f"d: {d}")

        if ls[-1][0] < d[0]:
            ls.append(d)
        else:
            for num in range(2, len(ls)):
                if ls[num][0] >= d[0]:
                    break
            ls.insert(num, d)
        ls.pop(0)
        ls.pop(0)

    return ls[0][1]


def fn_cod(st, el, ls_haf=None):
    ls_haf = [] if ls_haf is None else ls_haf

    if isinstance(el, str):
        ls_haf.append((el, st))
    else:
        fn_cod(st + "0", el[0], ls_haf)
        fn_cod(st + "1", el[1], ls_haf)

    return ls_haf


def make_dict(text):
    ls = make_tree(text)
    print(f"ls: {ls}")

    ls_haf = fn_cod("", ls)
    print(f"ls_haf: {ls_haf}")

    dc_haf = dict(ls_haf)
    print(f"dc_haf: {dc_haf}")

    return dc_haf


def compress(text, dc_haf, index="-"):
    st_res = [f"{index}".join(dc_haf[ch] for ch in text)]
    return st_res[0]


def decompress(text, dc_haf, index="-"):
    text = text.replace(index, "")
    dc_decode = {dc_haf[key]: key for key in dc_haf}
    print(f"dc_decode: {dc_decode}")

    st_res = ""
    while len(text) > 0:
        num = 1
        while text[:num] not in dc_decode:
            num += 1

        print(f"\ntext: {text[:num]}, num: {num}")
        st_res += dc_decode[text[:num]]
        print(f"\nst_res: {st_res}")
        text = text[num:]
    return st_res


if __name__ == "__main__":
    data = "preved medved"

    out = count_of_letters(data)
    print(out)

    tr = make_tree(data)
    # print(tr)

    dc = make_dict(data)
    # print(dc)

    compressed_text = compress(data, dc)
    print(compressed_text)

    decompressed_text = decompress(compressed_text, dc)
    print(decompressed_text)

# https://www.youtube.com/watch?v=2tqieMDTA4w&list=PLysMDSbb9Hcyxwq966ET1_6dXkNF_PW0L&index=4


def max_sub_len_one(s):
    max_len = 0

    for L in range(len(s) - 1):
        # print(f"L= {L}")
        for R in range(L, len(s)):
            # print(f"R= {R}")
            part = s[L : R + 1]
            print(f"part= {part}")
            if len(part) == len(set(part)):
                max_len = max(max_len, len(part))

    return max_len


def max_subs_len_two(s):
    seen = {}
    max_length = 0
    start = 0

    for n, el in enumerate(s):
        print(f"n= {n}, el= {el}")
        if el in seen:
            start = max(start, seen[el] + 1)
            print(f"n= {n}, el= {el}")
            print(f"seen_el= {seen[el]}")
        seen[el] = n
        max_length = max(max_length, n - start + 1)

        print(f"seen= {seen}")
        print(f"start= {start}")

    return max_length


if __name__ == "__main__":
    x = max_sub_len_one("abca")
    print(x)

    print("*" * 200)

    y = max_subs_len_two("abcabcd")
    print(y)

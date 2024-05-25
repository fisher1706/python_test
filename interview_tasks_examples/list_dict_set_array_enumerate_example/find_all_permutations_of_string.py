def get_permutations(string):
    if len(string) <= 1:
        return set(string)
    smaller = get_permutations(string[1:])
    print(f"smaller: {smaller}")
    perms = set()
    for x in smaller:
        for pos in range(0, len(x) + 1):
            perm = x[:pos] + string[0] + x[pos:]
            # print(f"perm: {perm}")
            perms.add(perm)
    return perms


if __name__ == "__main__":
    print(get_permutations("nan"))

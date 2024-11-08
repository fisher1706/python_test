# https://www.youtube.com/watch?v=qzbmxG7sYa4&list=PLysMDSbb9Hcyxwq966ET1_6dXkNF_PW0L&index=3


def find_disappeared_numbers_one(nums):
    nums = set(nums)
    mn = min(nums)
    mx = max(nums)
    rad = set(range(mn, mx))
    return rad - nums


def find_disappeared_numbers_two(nums):
    ch = [0] * len(nums)

    # пример с 4: 4 - 1 = 3 -> на ch[3] = 1, если после прогона всех чисел ch[n] = 0 -> n - нет в списке
    for el in nums:
        ch[el - 1] += 1
        print(f"el: {el}")
        print(f"ch: {ch}")

    net = []
    for n in range(len(ch)):
        if ch[n] == 0:
            net.append(n + 1)

    return net


if __name__ == "__main__":
    data = [4, 3, 2, 7, 8, 2, 3, 1]

    out = find_disappeared_numbers_one(data)
    print(out)
    print("*" * 200)

    out_two = find_disappeared_numbers_two(data)
    print(out_two)
    print("*" * 200)

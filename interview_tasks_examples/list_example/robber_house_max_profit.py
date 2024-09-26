# https://www.youtube.com/watch?v=VQvyqrJltcU


def robber(houses: list[int]) -> int:
    if len(houses) == 0:
        return 0
    elif len(houses) == 1:
        return 1

    dp = [0] * len(houses)
    dp[0] = houses[0]
    dp[1] = max(houses[0], houses[1])

    for i in range(2, len(houses)):
        dp[i] = max(dp[i - 1], houses[i] + dp[i - 2])
        i += 1

    return dp[-1]


if __name__ == "__main__":
    data = [4, 11, 10, 1, 2, 8, 5]

    out = robber(data)
    print(out)

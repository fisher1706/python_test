# https://www.youtube.com/watch?v=-59FbGWsCgI
def temperature(days: list):
    answer = [0] * len(days)

    for i in range(len(days)):
        for j in range(i + 1, len(days)):
            if days[j] > days[i]:
                answer[i] = j - i
                break

    return answer


if __name__ == "__main__":
    data = [13, 12, 15, 11, 9, 12, 16]

    out = temperature(data)
    print(out)

# https://www.youtube.com/watch?v=-59FbGWsCgI

from typing import List


def temperature(days: list):
    answer = [0] * len(days)

    for i in range(len(days)):
        for j in range(i + 1, len(days)):
            if days[j] > days[i]:
                answer[i] = j - i
                break

    return answer


def temperature_with_stack(days: List[int]) -> List[int]:
    answer = [0] * len(days)
    stack = []  # Stack to store indices of days

    for i, current_temp in enumerate(days):
        while stack and days[stack[-1]] < current_temp:
            prev_day = stack.pop()
            answer[prev_day] = i - prev_day
        stack.append(i)

    return answer


if __name__ == "__main__":
    data = [13, 12, 15, 11, 9, 12, 16]

    out = temperature(data)
    print(out)

    out_stack = temperature_with_stack(data)
    print(out_stack)

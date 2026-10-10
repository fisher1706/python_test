""" Given a string, find the first non-repeating character in it and return its index.
If it doesn't exist, return -1. # Note: all the input strings are already lowercase.
For example,
    'aassdd rggt' -> 6
    'aaaaaaa'-> -1
    'abba' -> -1 """


def find_non_repeating(some_str):
    counts = {}

    # Count occurrences
    for char in some_str:
        counts[char] = counts.get(char, 0) + 1

    print(counts)

    # Find first non-repeating character
    for index, char in enumerate(some_str):
        if counts[char] == 1:
            return index

    return -1


if __name__ == '__main__':
    print(find_non_repeating("abcba"))         # 2
    # print(find_non_repeating("aassdd rggt"))   # 6
    # print(find_non_repeating("aaaaaaa"))       # -1
    # print(find_non_repeating("abba"))          # -1

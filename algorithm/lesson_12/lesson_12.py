# https://www.youtube.com/watch?v=rEPggzaPoUw&list=PLRDzFCPr95fK7tr47883DFUbm4GeOjjc0&index=13
# https://www.youtube.com/watch?v=7g-WEBj3igk


def levenshtein(a: str, b: str) -> int:
    f = [[i + j if i * j == 0 else 0 for j in range(len(b) + 1)] for i in range(len(a) + 1)]
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                f[i][j] = f[i - 1][j - 1]
            else:
                f[i][j] = 1 + min(f[i - 1][j], f[i][j - 1], f[i - 1][j - 1])
    return f[len(a)][len(b)]


# https://www.youtube.com/watch?v=xAYmgdB-8Fg&list=PLtNPgSbW9TX7acrQa2LeBAMGxO5WRAVsz&index=70
def prefix_function(text: str) -> list:
    n = len(text)
    pi = [0] * n
    for i in range(1, n):
        j = pi[i - 1]
        while j > 0 and text[i] != text[j]:
            j = pi[j - 1]
        if text[i] == text[j]:
            j += 1
            pi[i] = j
    return pi


# https://www.youtube.com/watch?v=Vncv1JbOVwg
def kmp_search(main_string: str, sub_string: str, start_index: int = 0):
    pi = prefix_function(sub_string)  # Вычисление пи-функции для подстроки
    j = 0  # Индекс в подстроке
    # Проходим по основной строке
    for i in range(start_index, len(main_string)):
        # Пока j > 0 и символы не совпадают, используем пи-функцию для сдвига
        while j > 0 and main_string[i] != sub_string[j]:
            j = pi[j - 1]
        # Если символы совпадают, увеличиваем j
        if main_string[i] == sub_string[j]:
            j += 1
        # Если достигнут конец подстроки, нашли совпадение
        if j == len(sub_string):
            return i - j + 1  # Возвращаем индекс начала подстроки в основной строке
    return None  # Если подстрока не найдена


if __name__ == '__main__':
    str_1 = "level"
    str_2 = "avada kedavra"
    str_3 = "ACGA"
    main_str = "AAATGAACGAAAATCTGT"
    sub_str = "ACGA"

    # out = levenshtein(str_1, str_2)
    # print(out)

    # out = prefix_function(str_2)
    # print(out)

    out = prefix_function(str_3)
    print(out)
    #
    # out = kmp_search(main_str, sub_str)
    # print(out)

# https://www.youtube.com/watch?v=2tqieMDTA4w&list=PLysMDSbb9Hcyxwq966ET1_6dXkNF_PW0L&index=3

def max_subs_len(s):
    seen = {}
    max_length = 0
    start = 0

    for n, el in enumerate(s):
        if el in seen:
            start = max(start, seen[el] + 1)
        seen[el] = n
        max_length = max(max_length, n - start + 1)

    return max_length


"""
Объяснение
Инициализация:

seen: словарь для хранения индексов символов, которые мы уже встретили.
max_length: переменная для отслеживания максимальной длины подстроки без повторяющихся символов.
start: переменная для отслеживания начала текущей подстроки.
Итерация по строке:

enumerate(s): позволяет итерировать по строке s и получать как индекс n, так и сам символ el.
Проверка повторяющихся символов:

Если символ el уже был встречен (есть в словаре seen), обновляем start, чтобы начать новую подстроку после последнего 
встреченного повторяющегося символа.
start = max(start, seen[el] + 1): обновляем start только в том случае, если предыдущая встреча этого символа находится 
ближе к текущему началу подстроки.
Обновление словаря:

Обновляем индекс текущего символа el в словаре seen.
Обновление максимальной длины:

max_length = max(max_length, n - start + 1): вычисляем длину текущей подстроки и обновляем max_length, если текущая 
подстрока длиннее предыдущей максимальной.
Возвращение результата:

Возвращаем максимальную длину подстроки без повторяющихся символов.
Пример
Рассмотрим пример с строкой "abcabcbb":

a: max_length = 1, seen = {'a': 0}
b: max_length = 2, seen = {'a': 0, 'b': 1}
c: max_length = 3, seen = {'a': 0, 'b': 1, 'c': 2}
a: start = 1, max_length = 3, seen = {'a': 3, 'b': 1, 'c': 2}
b: start = 2, max_length = 3, seen = {'a': 3, 'b': 4, 'c': 2}
c: start = 3, max_length = 3, seen = {'a': 3, 'b': 4, 'c': 5}
b: start = 5, max_length = 3, seen = {'a': 3, 'b': 6, 'c': 5}
b: start = 7, max_length = 3, seen = {'a': 3, 'b': 7, 'c': 5}
"""


# https://www.youtube.com/watch?v=kzPUYPfzT9A


def longest_substring(s: str) -> int:
    answer = 0

    for left in range(len(s)):
        for right in range(left, len(s)):
            is_acceptable = True
            char_set = set()

            for i in range(left, right + 1):
                if s[i] in char_set:
                    is_acceptable = False
                    break
                char_set.add(s[i])
            if is_acceptable and answer < right - left + 1:
                answer = right - left + 1

    return answer


def long_substring_two(s: str) -> int:
    answer, left, right = 0, 0, 0
    hash_set = set()

    while right < len(s):
        c = s[right]
        if c not in hash_set:
            hash_set.add(c)
            answer = max(answer, right - left + 1)
            right += 1
        else:
            while c in hash_set:
                hash_set.remove(s[left])
                left += 1

    return answer


if __name__ == '__main__':
    print(max_subs_len("abcabcbb"))

    data = "abcabcbb"

    out = longest_substring(data)
    print(out)

    out = long_substring_two(data)
    print(out)

def get_permutations(string):
    if len(string) <= 1:
        return set(string)
    smaller = get_permutations(string[1:])
    print(f"smaller: {smaller}")

    perms = set()
    for x in smaller:
        for pos in range(0, len(x) + 1):
            perm = x[:pos] + string[0] + x[pos:]
            print(f"perm: {perm}")
            perms.add(perm)
    return perms


"""
Ваш код реализует функцию для получения всех перестановок строки. Давайте разберем его пошагово и 
приведем окончательную версию:

Объяснение
Базовый случай: если строка пустая или состоит из одного символа, возвращаем множество с этим символом.
Рекурсивный случай: берем все перестановки оставшейся части строки и добавляем первый символ строки на каждую 
возможную позицию во всех этих перестановках.
Результат: возвращаем множество всех полученных перестановок.
Пример
Рассмотрим пример с входной строкой "abc":

get_permutations("abc")
get_permutations("bc")
get_permutations("c")
Базовый случай: {"c"}
Перестановки для "bc": добавляем "b" на каждую позицию в "c"
bc
cb
Перестановки для "abc": добавляем "a" на каждую позицию в "bc" и "cb"
abc
bac
bca
acb
cab
cba

"""


if __name__ == "__main__":
    print(get_permutations("nan"))

    data = [1, 2, 3]
    print(data[:1])
    print(data[1:])

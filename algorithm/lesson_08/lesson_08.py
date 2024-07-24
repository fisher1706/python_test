# https://www.youtube.com/watch?v=2XFaK3bgT7w
# Полезно посмотреть картинку в этой же папке для обхода/траектории

def generate_numbers(n: int, m: int, prefix=None):
    """
    Генерирует все числа (с лидирующими незначащими нулями) в N-ричной
    системе счисления (N <= 10) длины M
    """

    # Инициализация префикса, если он не передан
    prefix = prefix or []

    # Если m равно 0, вывести текущий префикс
    if m == 0:
        print(f"prefix: {prefix}")
        return

    # Перебор всех цифр от 0 до n-1
    for digit in range(n):
        # Добавление цифры в префикс
        prefix.append(digit)
        # Рекурсивный вызов с уменьшением m на 1
        generate_numbers(n, m - 1, prefix)
        # Удаление последней цифры для возврата к предыдущему состоянию префикса
        prefix.pop()


"""
Функция должна генерировать все возможные последовательности длины m из чисел от 0 до n-1 включительно.
Пояснение исправленного кода
Инициализация префикса:
Если prefix не передан, он инициализируется пустым списком.
Базовый случай:
Если m равно 0, текущий префикс выводится и функция завершает выполнение для данной ветки рекурсии.
Рекурсивный случай:
Цикл перебирает все цифры от 0 до n-1.
Каждая цифра добавляется в префикс, и функция вызывается рекурсивно с уменьшением m на 1.
После рекурсивного вызова последняя цифра удаляется из префикса (это важно для корректной работы рекурсии).
"""


def generate_permutation(n: int, m: int = -1, prefix=None):
    """
    Генерация всех перестановок N чисел в M позициях, с префиксом
    prefix.
    """
    if m == -1:
        m = n

    prefix = prefix or []

    if m == 0:
        print(prefix)
        return

    for number in range(1, n + 1):
        if find(number, prefix):
            continue
        prefix.append(number)
        generate_permutation(n, m - 1, prefix)
        prefix.pop()


def find(num: int, data: list) -> bool:
    flag = False
    for x in data:
        if num == x:
            flag = True
            break
        return flag


if __name__ == '__main__':
    generate_numbers(3, 2)
    print("*" * 200)

    generate_permutation(3)

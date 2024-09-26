# https://www.youtube.com/watch?v=v5Y4vQ824cI


# O(n^3)
def find_sublist_from_list_with_sum_equal_number_one(nums: list, k: int) -> int:
    answer = 0
    for start in range(len(nums)):
        for end in range(start, len(nums)):
            subarray_sum = 0
            for i in range(start, end + 1):
                subarray_sum += nums[i]
            if subarray_sum == k:
                answer += 1
    return answer


# O(n^2)
def find_sublist_from_list_with_sum_equal_number_two(nums: list, k: int) -> int:
    answer = 0
    for start in range(len(nums)):
        subarray_sum = 0
        for i in range(start, len(nums)):
            subarray_sum += nums[i]
            if subarray_sum == k:
                answer += 1
    return answer


# O(n^1)
def find_sublist_from_list_with_sum_equal_number_three(nums: list, k: int) -> int:
    answer = 0
    subarray_sum = 0
    prefix_sum_count = {0: 1}

    for i in range(len(nums)):
        subarray_sum += nums[i]
        to_remove = subarray_sum - k
        answer += prefix_sum_count.get(to_remove, 0)
        prev_count = prefix_sum_count.get(subarray_sum, 0)
        prefix_sum_count[subarray_sum] = prev_count + 1
    return answer


# https://www.youtube.com/watch?v=3g3kx08C0uE&list=PLysMDSbb9Hcyxwq966ET1_6dXkNF_PW0L&index=8


def func(data_in: list, number: int) -> int:
    hsh = {0: 1}
    cnt = 0
    x = 0
    for el in data_in:
        x += el
        cnt += hsh.get(x - number, 0)
        hsh[x] = hsh.get(x, 0) + 1

    print(hsh)
    return cnt


"""
Ваш код реализует функцию, которая находит количество подмассивов в списке data, сумма элементов которых равна number. 
Функция использует хеш-таблицу для отслеживания префиксных сумм и работает за линейное время 
O(n). Вот объяснение работы функции:

Объяснение
Инициализация переменных:

hsh: словарь для хранения количества раз, когда встречается каждая префиксная сумма. Изначально содержит {0: 1}, 
что учитывает подмассив, который начинается с первого элемента.
cnt: счетчик подмассивов, сумма элементов которых равна number.
x: текущая префиксная сумма.
Итерация по списку:

Для каждого элемента el в списке data:
Добавляем el к текущей префиксной сумме x.
Увеличиваем cnt на количество раз, когда префиксная сумма x - number уже встречалась ранее 
(если такая сумма есть в словаре hsh).
Обновляем словарь hsh, увеличивая количество для текущей префиксной суммы x.
Пример
Рассмотрим пример:

Пошаговый разбор
el = 1, x = 1, hsh = {0: 1, 1: 1}, cnt = 0
el = 1, x = 2, cnt += hsh.get(2 - 2, 0) => cnt = 1, hsh = {0: 1, 1: 1, 2: 1}
el = 1, x = 3, cnt += hsh.get(3 - 2, 0) => cnt = 2, hsh = {0: 1, 1: 1, 2: 1, 3: 1}
Функция возвращает 2, так как в списке data есть два подмассива, 
сумма элементов которых равна numer (это подмассивы [1, 1] и [1, 1]).

Заключение
Этот алгоритм работает за линейное время 
O(n) и использует линейную память для хранения префиксных сумм. Функция корректно решает задачу нахождения 
количества подмассивов с заданной суммой.
"""


if __name__ == "__main__":
    data = [7, 2, -5, 1, 1, -1, 5, -5]
    n = 5

    out = find_sublist_from_list_with_sum_equal_number_one(data, n)
    print(out)

    out = find_sublist_from_list_with_sum_equal_number_two(data, n)
    print(out)

    out = find_sublist_from_list_with_sum_equal_number_three(data, n)
    print(out)

    m = [1, 1, 1]
    n = 2

    out = func(m, n)
    print(out)

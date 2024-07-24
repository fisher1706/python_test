def qsort(arr):
    if len(arr) <= 1:
        return arr
    return (
        qsort([x for x in arr[1:] if x < arr[0]])
        + arr[0:1]
        + qsort([x for x in arr[1:] if x >= arr[0]])
    )


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]  # выбор опорного элемента
        # print(f"pivot: {pivot}")
        left = [x for x in arr if x < pivot]
        # print(f"left: {left}")
        middle = [x for x in arr if x == pivot]
        # print(f"middle: {middle}")
        right = [x for x in arr if x > pivot]
        # print(f"right: {right}")
        return quicksort(left) + middle + quicksort(right)


"""
Функция qsort (quick sort, или быстрая сортировка) в Python не встроена в стандартную библиотеку, 
но её можно легко реализовать. Быстрая сортировка — это эффективный алгоритм сортировки, работающий по принципу 
"разделяй и властвуй". Основная идея состоит в следующем:

Выбирается опорный элемент (pivot).
Массив разделяется на две части: элементы, меньшие опорного, и элементы, большие или равные опорному.
Рекурсивно применяется быстрая сортировка к двум подмассивам.

Базовый случай: Если длина массива меньше или равна 1, массив уже отсортирован, и его можно возвращать.
Выбор опорного элемента: Опорный элемент выбирается как элемент, находящийся в середине массива (arr[len(arr) // 2]).
Разделение массива:
left: Содержит элементы, меньшие опорного.
middle: Содержит элементы, равные опорному.
right: Содержит элементы, большие опорного.
Рекурсивная сортировка: Функция вызывает сама себя для сортировки левой и правой частей, а затем объединяет результаты.
Эта реализация довольно проста и понятна, но не оптимальна по использованию памяти, так как создаёт новые списки 
на каждой рекурсивной итерации. Более оптимальная версия использует сортировку на месте, которая не требует 
дополнительной памяти для хранения промежуточных массивов. Однако для понимания основ алгоритма 
данная версия подходит отлично.
"""


# https://www.youtube.com/watch?v=TI0u7o5I_Yo&list=PLuW7Z72R04bia6ohD5ELVhNZXm5gdU8s5&index=1

def quick_sort(array: list, reverse: bool = True) -> list:
    if len(array) <= 1:
        return array

    pivot = array[0]
    lover_array = [el for el in array if el < pivot]
    higher_array = [el for el in array if el > pivot]

    result = (
            quick_sort(lover_array, reverse=reverse) +
            [el for el in array if el == pivot] +
            quick_sort(higher_array, reverse=reverse)) if reverse \
        else (
            quick_sort(higher_array, reverse=reverse) +
            [el for el in array if el == pivot] +
            quick_sort(lover_array, reverse=reverse))
    return result


if __name__ == "__main__":
    data_one = [3, 6, 8, 10, 1, 2, 1]

    print(qsort(data_one))
    print(quicksort(data_one))

    data_two = [5, 7, 2, 4, 8, 11, 3, 5]

    out = quick_sort(data_two)
    print(out)

    out = quick_sort(data_two, reverse=False)
    print(out)

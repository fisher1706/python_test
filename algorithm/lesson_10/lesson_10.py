def left_bound(a: list, key: int) -> int:
    left = -1
    right = len(a)

    while right - left > 1:
        middle = (left + right) // 2
        if a[middle] < key:
            left = middle
        else:
            right = middle

    return left


def right_bound(a: list, key: int):
    left = -1
    right = len(a)

    while right - left > 1:
        middle = (left + right) // 2
        if a[middle] <= key:
            left = middle
        else:
            right = middle

    return right


def binary_search_iterative(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        # Проверка, если средний элемент - искомый
        if arr[mid] == target:
            return mid
        # Если искомый элемент меньше среднего, ищем в левой половине
        elif arr[mid] > target:
            right = mid - 1
        # Если искомый элемент больше среднего, ищем в правой половине
        else:
            left = mid + 1

    # Элемент не найден
    return -1


def binary_search_recursive(arr, target, left, right):
    if left > right:
        return -1

    mid = left + (right - left) // 2

    # Проверка, если средний элемент - искомый
    if arr[mid] == target:
        return mid
    # Если искомый элемент меньше среднего, ищем в левой половине
    elif arr[mid] > target:
        return binary_search_recursive(arr, target, left, mid - 1)
    # Если искомый элемент больше среднего, ищем в правой половине
    else:
        return binary_search_recursive(arr, target, mid + 1, right)


if __name__ == "__main__":
    my_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    my_target = 7

    result = binary_search_iterative(my_arr, my_target)
    print(
        f"Элемент найден на индексе: {result}" if result != -1 else "Элемент не найден"
    )

    result = binary_search_recursive(my_arr, my_target, 0, len(my_arr) - 1)
    print(
        f"Элемент найден на индексе: {result}" if result != -1 else "Элемент не найден"
    )

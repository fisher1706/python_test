def find_pairs(my_list, number):
    pairs = []
    for i, el_1 in enumerate(my_list):
        for j, el_2 in enumerate(my_list[i + 1:]):
            if el_1 + el_2 == number:
                pairs.append((el_1, el_2))
    return pairs


# https://www.youtube.com/watch?v=JtMuXmmDl9s
def find_pairs_with_hash_set(my_list, number):
    # Множество для хранения уже встреченных чисел
    hsh = set()
    # Список для хранения найденных пар
    out = []

    # Проходим по каждому элементу списка
    for num in my_list:
        # Вычисляем необходимое число для текущего элемента
        number_to_find = number - num
        # Проверяем, есть ли необходимое число в множестве
        if number_to_find in hsh:
            # Если есть, добавляем пару в список результата
            out.append([number_to_find, num])
        # Добавляем текущий элемент в множество
        hsh.add(num)

    return out


# https://www.youtube.com/watch?v=LRbpzSgBjEE&list=PLysMDSbb9Hcyxwq966ET1_6dXkNF_PW0L&index=7
# https://www.youtube.com/watch?v=JtMuXmmDl9s


def find_different_sum(array, number):
    left = 0
    right = len(array) - 1

    while True:
        try:
            amount = array[left] + array[right]
            if amount > number:
                right -= 1
            elif amount < number:
                left += 1
            elif amount == number:
                print(array[left], array[right])
                break
        except Exception as e:
            print(e)
            print("Zero")
            break


if __name__ == "__main__":
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    n = 5
    print(find_pairs(data, n))
    print("*" * 200)

    x = find_pairs_with_hash_set(data, n)
    print(x)
    print("*" * 200)

    data = [-4, -1, 0, 2, 3, 4, 7, 9]
    k = 10
    find_different_sum(data, k)
    print("*" * 200)

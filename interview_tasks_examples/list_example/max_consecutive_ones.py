# https://www.youtube.com/watch?v=VWEFo37RP44&list=PLysMDSbb9Hcyxwq966ET1_6dXkNF_PW0L&index=4

def func(data: list, number: int):
    left = right = max1 = zeros = 0
    while right < len(data):
        if data[right] == 0:
            zeros += 1
        while zeros > number:
            if data[left] == 0:
                zeros -= 1
            left += 1
        max1 = max(max1, right - left + 1)
        right += 1
    print(max1)


"""
Ваш код реализует функцию, которая находит длину самой длинной подстроки, 
содержащей не более number нулей в списке data. Давайте разберем его более подробно:

Объяснение
Инициализация переменных:

left и right: указатели на границы текущего окна.
max1: переменная для отслеживания максимальной длины подстроки, соответствующей условиям.
zeros: счетчик нулей в текущем окне.
Основной цикл:

Цикл while right < len(data) итерирует через весь список data с помощью указателя right.
Обработка правого указателя:

Если текущий элемент data[right] равен нулю, увеличиваем счетчик zeros.
Контроль количества нулей:

Пока количество нулей в текущем окне больше, чем number, передвигаем left вправо, 
уменьшая счетчик нулей, если data[left] равен нулю.
Обновление максимальной длины:

На каждой итерации обновляем max1, если текущая длина окна больше текущего максимума.
Увеличение правого указателя:

Увеличиваем right для перехода к следующему элементу.

Пошаговый разбор:
right = 0, data[right] = 1, zeros = 0, max1 = 1
right = 1, data[right] = 0, zeros = 1, max1 = 2
right = 2, data[right] = 1, zeros = 1, max1 = 3
right = 3, data[right] = 1, zeros = 1, max1 = 4
right = 4, data[right] = 0, zeros = 2, max1 = 5
right = 5, data[right] = 1, zeros = 2, max1 = 6
right = 6, data[right] = 0, zeros = 3, начинаем передвигать left, пока zeros <= number
left = 1, data[left] = 0, zeros = 2
right = 7, data[right] = 1, zeros = 2, max1 = 7
Дальнейшие итерации не дадут большую длину подстроки.
Оптимизация
Ваш код уже оптимален и использует подход с двумя указателями (скользящее окно), который работает за линейное время 
O(n). Функция корректно решает задачу нахождения максимальной длины подстроки с заданным количеством нулей.
"""


if __name__ == '__main__':
    nums = [1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1]
    k = 2

    func(nums, k)

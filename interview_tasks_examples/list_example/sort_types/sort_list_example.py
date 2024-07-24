numbers = [7, 1, 4, 8]
sorted_number = sorted(numbers)
print(sorted_number)

numbers.sort()
print(numbers)


"""
В Python есть два способа сортировки списка: встроенный метод списка list.sort() и встроенная функция sorted().
⏺ sorted() принимает итерируемый объект и возвращает новый отсортированный список, не изменяя исходный;
⏺ list.sort() сортирует список на месте, то есть изменяет исходный список.
"""
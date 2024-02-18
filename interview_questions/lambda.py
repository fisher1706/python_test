"""
Лямбда-функция (также известна как "анонимная функция") - это функция, которая определяется в одной строке кода
без использования ключевого слова def. Она может быть использована вместо обычной функции,
когда требуется быстрое определение небольшой функции. Использует неявный ретерн.

Функция map применяет функцию к каждому элементу последовательности и возвращает итератор с результатами.
"""

numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, numbers))


if __name__ == '__main__':
    print(squares)

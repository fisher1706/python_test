"""
Индекс Хирша (или h-индекс) — это метрика, которая используется для оценки продуктивности ученого на основе
количества публикаций и цитирований. Индекс h равен максимальному числу h таких, что у автора есть как минимум
h публикаций, каждая из которых была процитирована хотя бы h раз.

Объяснение
Сортировка:
Сначала сортируем список цитирований в порядке убывания.
Вычисление h-индекса:
Итерируемся по отсортированному списку.
Для каждого элемента проверяем, больше ли он или равен его индексу (сдвинутому на 1, потому что индексы начинаются с 0).
Если условие выполняется, обновляем значение h.
Если условие не выполняется, прерываем цикл, так как дальнейшие элементы будут еще меньше.
Этот подход обеспечивает вычисление h-индекса за время
O(nlogn) за счет сортировки и
O(n) за счет прохода по списку, что является достаточно эффективным для большинства практических случаев.
"""


def h_index(citations):
    citations.sort(reverse=True)
    h = 0
    for i, c in enumerate(citations):
        if c >= i + 1:
            h = i + 1
        else:
            break
    return h


if __name__ == '__main__':
    # Список цитирований
    data = [3, 0, 6, 1, 5]

    # Вычисление h-индекса
    print(h_index(data))  # Должно вывести: 3

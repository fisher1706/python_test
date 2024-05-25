from terminaltables import AsciiTable

"""
Для создания и отображения таблиц в формате ASCII в Python можно использовать библиотеку terminaltables.
Она предоставляет простой способ создания таблиц для отображения в терминале. Ниже приведены шаги по установке
и использованию библиотеки terminaltables для создания ASCII таблиц.
"""


# Определение данных для таблицы
data = [
    ['Header 1', 'Header 2'],
    ['Row 1, Col 1', 'Row 1, Col 2'],
    ['Row 2, Col 1', 'Row 2, Col 2']
]

# Создание таблицы
table_one = AsciiTable(data)

table_two = AsciiTable(data)
table_two.title = 'My Table Title'  # Добавление заголовка таблицы


if __name__ == '__main__':
    # Печать таблицы в терминал
    print(table_one.table)
    print(table_two.table)

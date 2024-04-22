"""
Types of SQL Inner and Outer Joins:

- Inner Join:
  Retrieves rows from both tables where there is a match between the specified columns.
  This is the most commonly used type of join.

- Left Outer Join:
  Returns all rows from the left table and the matched rows from the right table.
  It's useful when you want to keep unmatched records from the left table.

- Right Outer Join:
  Returns all rows from the right table and the matched rows from the left table.
  It's beneficial for scenarios where unmatched records from the right table need to be preserved.

- Full Outer Join:
  Combines rows from both tables, whether they have a match or not. This join type ensures that no data is left behind,
  providing a comprehensive view of information across tables.


Типы внутренних и внешних соединений SQL:

- Внутреннее соединение:
  извлекает строки из обеих таблиц, в которых есть совпадения между указанными столбцами.
  Это наиболее часто используемый тип соединения.

- Левое внешнее соединение:
  возвращает все строки из левой таблицы и совпадающие строки из правой таблицы.
  Это полезно, если вы хотите сохранить несовпадающие записи из левой таблицы.

- Правое внешнее соединение:
  возвращает все строки из правой таблицы и совпадающие строки из левой таблицы.
  Это полезно в сценариях, где необходимо сохранить несовпадающие записи из нужной таблицы.

- Полное внешнее соединение:
  объединяет строки из обеих таблиц независимо от того, есть ли у них совпадение или нет.
  Этот тип соединения гарантирует, что никакие данные не останутся позади,
  обеспечивая комплексное представление информации по таблицам.
"""
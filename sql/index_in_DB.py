"""
Индексы – это специальные структуры данных, которые используются для ускорения операций выборки (retrieval) и
поиска данных в таблице. Они подобны индексам в книге: вместо того, чтобы перелистывать всю книгу
(или всю таблицу данных) для поиска нужной информации,
вы можете использовать индекс для быстрого нахождения необходимых данных.

Зачем нужны
Индексы существенно ускоряют поиск и выборку данных, особенно в больших таблицах.
Без индексов база данных должна была бы осуществлять "полное сканирование таблицы" (full table scan),
что очень ресурсоемко и медленно, особенно для больших объемов данных.
Однако стоит учитывать, что создание и поддержание индексов также требует дополнительных ресурсов,
включая место на диске и время на обновление индекса при изменении данных в таблице.

Как работают индексы
Существуют различные типы индексов, и они могут быть реализованы по-разному в зависимости от системы управления
базами данных (СУБД), но обычно они используют структуры данных, такие как B-деревья или хеш-таблицы,
для эффективного хранения и поиска данных.

Например, если вы создаете индекс для столбца "Фамилия" в таблице с записями сотрудников,
СУБД создаст структуру данных (например, B-дерево), которая позволит быстро находить записи по значению фамилии,
не перебирая каждую запись в таблице.

CREATE INDEX idx_lastname ON employees (lastname);

Эта SQL-команда создает индекс idx_lastname для столбца lastname в таблице employees.
После создания этого индекса запросы, которые ищут сотрудников по фамилии, будут выполняться значительно быстрее.

Индексы – это структуры, которые ускоряют поиск данных в таблицах, работая подобно индексам в книге.
Они особенно полезны для больших таблиц и сложных запросов.
"""

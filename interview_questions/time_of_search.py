"""
Скорость поиска зависит от контекста использования и объема данных, но в общем случае:

Поиск в списке (list):

- Время выполнения поиска в списке зависит от количества элементов в списке и способа поиска.
- Линейный поиск в списке (без предварительной сортировки) имеет сложность
  O(n), где n - количество элементов в списке.
- Если список отсортирован и используется бинарный поиск, время выполнения будет
  O(log n), что быстрее линейного поиска, особенно для больших списков.

Поиск в словаре (dict):

- Поиск в словаре в среднем выполняется за
  O(1) по времени, независимо от количества элементов в словаре.
  Однако при этом необходимо учитывать возможные коллизии хэш-функций.
- Словари используют хэш-таблицы, что позволяет выполнять поиск элемента по ключу за постоянное время.
- Поэтому, для поиска по ключу словарь может быть быстрее списка, особенно при большом количестве элементов.

- Поиск в кортеже (tuple):

- Поиск в кортеже выполняется аналогично поиску в списке, так как кортежи также являются упорядоченными коллекциями.
- Время выполнения поиска зависит от способа поиска и количества элементов в кортеже.
- Если кортеж содержит отсортированные элементы и используется бинарный поиск, время выполнения будет
  O(log n).

Итак, для быстрого поиска по ключу наилучшим выбором обычно является словарь (dict).
Если данные упорядочены и часто меняются, то список (list) может быть более эффективным.
Если данные не предполагается изменять и упорядочены,
а поиск производится только по значению, то кортеж (tuple) может быть быстрее.
"""
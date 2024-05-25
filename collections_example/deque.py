from collections import deque


"""
deque - потокобезопасна, быстрая вставка справа и слева

Преимущества list перед deque

1. Прямой доступ по индексу (случайный доступ):
Поддерживает O(1) время доступа к элементам по индексу, 
что позволяет быстро и эффективно обращаться к любому элементу в списке.
deque: Хотя deque поддерживает доступ по индексу, его время доступа O(n) в худшем случае, 
так как deque оптимизирован для добавления и удаления элементов с обеих сторон.

2. Меньшее использование памяти:
Обычно потребляет меньше памяти по сравнению с deque, 
так как list оптимизирован для хранения данных с минимальными накладными расходами.
deque: Может использовать больше памяти из-за необходимости хранения дополнительных структур 
для поддержки эффективного добавления и удаления элементов.

3. Больше встроенных методов:
Предоставляет более широкий набор встроенных методов для работы с элементами, 
таких как sort(), reverse(), index(), count() и другие, 
что делает list более универсальным для различных операций с последовательностями.
deque: Предоставляет ограниченный набор методов, оптимизированных для операций с добавлением и удалением.

4. Удобство использования для различных операций:
Легко использовать для различных типов операций, таких как создание срезов, 
конкатенация, повторение, итерирование и другие.

deque: Основное преимущество заключается в добавлении и удалении элементов с обоих концов, 
что делает его менее универсальным для других типов операций.

Когда использовать list вместо deque

Когда требуется быстрый доступ к элементам по индексу.
- Когда операции добавления и удаления происходят преимущественно в конце последовательности.
- Когда необходимы встроенные методы для работы с последовательностями.
- Когда важна экономия памяти.
- Когда требуется поддержка срезов и других операций, специфичных для списков.

Заключение
Оба типа коллекций имеют свои области применения. list лучше всего подходит для сценариев, 
требующих частого доступа по индексу, использования встроенных методов и работы с последовательностями в целом. 
deque лучше всего подходит для сценариев, где часто происходят операции добавления и удаления с 
обоих концов последовательности. Выбор между ними зависит от конкретных требований и характеристик задачи.
"""


a_deque = deque()
a_deque.append(1)

b_deque = deque([1, 2, 3], maxlen=3)


def read_file_with_deque(filename="points.csv", max_len=2):
    with open(filename, 'r') as f:
        f_deque = deque(f, maxlen=max_len)

    for line in f_deque:
        print(line.rstrip())


if __name__ == '__main__':
    print(a_deque)
    a_deque.appendleft(2)
    print(a_deque)
    a_deque.popleft()
    print(a_deque)
    print("*" * 200)

    print(b_deque)
    b_deque.append(4)
    print(b_deque)
    print("*" * 200)

    read_file_with_deque()
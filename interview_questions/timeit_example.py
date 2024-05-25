import timeit


"""
timeit — это встроенный модуль в Python, который используется для измерения времени выполнения небольших 
фрагментов кода. Он особенно полезен для проведения микро-бенчмаркинга, чтобы сравнивать производительность различных 
подходов к решению одной и той же задачи.


Использование через командную строку:
python -m timeit -n 1000 "sum(range(100))"


Параметры timeit.timeit
- stmt: Код для выполнения, в виде строки. По умолчанию это "pass".
- setup: Код для настройки окружения перед выполнением основного кода, в виде строки. По умолчанию это "pass".
- globals: Словарь глобальных переменных. Используется для доступа к функциям и переменным, 
  определенным в глобальной области видимости.
- number: Количество выполнений основного кода. По умолчанию это 1_000_000.


Дополнительные советы
- Проверка кода на корректность:
    - Убедитесь, что код работает правильно, прежде чем измерять его время выполнения. 
      timeit не показывает ошибки выполнения, оно просто измеряет время.

- Измерение только значимых частей кода:
    - Убедитесь, что вы измеряете только ту часть кода, которая важна для вашего анализа производительности.

- Учитывание повторяемости:
    - Для более точных результатов выполняйте код несколько раз и усредняйте результаты.

- Использование repeat для более надежных измерений:
    - Функция timeit.repeat позволяет выполнить тест несколько раз и вернуть список времен выполнения. 
    Это помогает получить более надежные данные.
"""


# Использование в виде модуля в Python-коде:
def example_function():
    return sum(range(100))


# Измерение времени выполнения с подготовительным кодом:
setup_code = "from math import sqrt"
test_code = """
def compute():
    return [sqrt(i) for i in range(100)]
compute()
"""


if __name__ == '__main__':
    execution_time = timeit.timeit('example_function()', globals=globals(), number=1000)
    print(f"Execution time: {execution_time} seconds")

    execution_time = timeit.timeit(stmt=test_code, setup=setup_code, number=1000)
    print(f"Execution time for compute function: {execution_time} seconds")

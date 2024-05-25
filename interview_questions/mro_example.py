"""
MRO (Method Resolution Order) — это порядок, в котором Python ищет методы и атрибуты класса при их вызове.
Этот порядок особенно важен в контексте множественного наследования, когда класс наследует поведение и атрибуты от
нескольких родительских классов, и нужно четко определить, откуда именно брать эти атрибуты и
методы в случае их совпадения.

MRO определяет порядок, в котором интерпретатор будет искать методы и атрибуты при их вызове в контексте
множественного наследования. Это обеспечивает предсказуемость и избегает конфликтов
при наследовании от нескольких классов.

Зачем нужен MRO ?
MRO помогает избежать проблемы алмаза (diamond problem), которая возникает, когда два родительских класса наследуют
от одного и того же базового класса, а затем эти классы сливаются в один дочерний класс.
Без четко определенного MRO Python не смог бы автоматически решить, в каком порядке следует искать методы
и атрибуты среди родительских классов.

Как работает MRO ?
Python использует алгоритм C3 Linearization для определения MRO. Этот алгоритм гарантирует,
что порядок разрешения методов учитывает следующие условия:

✅ Подкласс всегда имеет приоритет перед родительским классом.
✅ Порядок родительских классов сохраняется.
✅ Если класс наследует от нескольких классов, порядок, указанный при наследовании, определяет приоритетности.

Можно узнать MRO любого класса, используя атрибут __mro__ или метод mro() у самого класса.

"""


class A:
    pass


class B(A):
    pass


class C(A):
    pass


class D(B, C):
    pass


if __name__ == "__main__":
    print(D.mro())
    print("*" * 300)

    print(D.__mro__)

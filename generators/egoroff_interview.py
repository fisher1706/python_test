# https://www.youtube.com/watch?v=8cMMO8fks-k&list=PLQAt0m1f9OHvv2wxPGSCWjgy1qER_FvB6&index=51
import asyncio

"""
Генератор в Python – это специальный тип функций, который позволяет вам возвращать значение и позже продолжить
выполнение функции с того места, где она была остановлена. Это достигается с помощью ключевого слова yield.

Главное отличие генератора от обычной функции заключается в том, что генератор возвращает итерируемый объект,
через который можно пройти только один раз. Это позволяет эффективно работать с данными,
не загружая полностью их в память. Это особенно полезно, когда вам нужно работать с большими объемами данных или
когда вы не знаете заранее, сколько элементов вам понадобится.

В этом примере функция "genf" является генератором.
Когда вы вызываете её, она не выполняет свой код сразу. Вместо этого, она возвращает итерируемый объект.
Когда вы итерируетесь через этот объект (например, используя цикл for),
код внутри функции выполняется до первого yield. Значение, которое следует за yield, возвращается в цикл.
При следующей итерации выполнение функции возобновляется сразу после yield и продолжается до следующего yield.

Использование генераторов позволяет сэкономить ресурсы, так как значения генерируются по мере необходимости,
а не хранятся в памяти.

[reset = yield current]
"""


def my_gen():
    out = 7
    for item in [43, 65, 32]:
        yield item
        print(f"out:= {out}")
        print(f"item:= {item}")
        out = out * 10 + 7


def fact(n):
    pr = 1
    for item in range(1, n + 1):
        pr = pr * item
        yield pr


"""
В асинхронных функциях (async def) используется await вместо yield, но концептуально это очень похоже. 
Когда функция достигает await, она возвращает управление вызывающей стороне, позволяя другим задачам выполняться, 
пока текущая задача находится в ожидании (например, ожидает ответа от сервера).

Здесь fetch_data является асинхронной функцией. Когда она достигает строки await asyncio.sleep(2), 
управление возвращается в main, позволяя выполнять другие операции, в то время как fetch_data находится в ожидании.

Таким образом, генераторы и асинхронные функции позволяют Python более эффективно использовать 
однопоточную модель исполнения, предоставляя механизм для конкурентного выполнения задач, особенно в ситуациях, 
когда много времени уходит на ожидание ввода/вывода.
"""


async def fetch_data():
    print('Start fetching')
    await asyncio.sleep(2)  # Имитация асинхронной задачи, например, запроса к серверу
    print('Done fetching')
    return {'data': 1}


async def main():
    print('Before fetching')
    result = await fetch_data()
    print('Result:', result)
    print('After fetching')


if __name__ == '__main__':
    s = my_gen()
    print(s)
    print(next(s))
    print(next(s))
    print(next(s))
    print("*" * 200)

    for i in fact(10):
        print(i, end=' ')

    print("*" * 200)

    asyncio.run(main())

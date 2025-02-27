git # check code for availability of mistakes
```shell
cd interview_questions && python -m py_compile lambda_with_filter.py
```
------------------------------------------------------------------------------------------------------------------------
# @classmethod - работает только с атрибутами класса - не может обращатья к локальным атрибутам экземпляра класса
# @staticmethod - нет доступа как к атрибутам класса - так и к атрибутам его экземпляра
# self method - есть доступ как к атрибутам класса так и к атрибутам экземпляра класса

------------------------------------------------------------------------------------------------------------------------
# МОДИФИКАТОРЫ ДОСТУПА К АТРИБУТАМ КЛАССА
# atr - public - доступ для всех 
# _atr - protected - доступ из класса и дочерних классов
# __atr - private - доступ только из класса

------------------------------------------------------------------------------------------------------------------------
# метод __iter__ используется для создания итератора, а метод __next__ используется для перехода к следующему элементу в 
# итерации __iter__ возвращает сам объект, а метод __next__ возвращает следующий элемент data каждый раз, 
# когда вызывается

------------------------------------------------------------------------------------------------------------------------
# контекстный менеджер в Python - это объект, который определяет вход и выход из контекста с 
# помощью методов enter() и exit(). Контекстный менеджер может быть использован в блоке "with" для 
# выполнения конкретных действий при входе и выходе из блока.

# Контекстный менеджер with: удобные конструкции, которые позволяют разработчику настраивать что-нибудь и разрывать 
# в автоматическом режиме. Например, вам может потребоваться открыть файл, вписать в него кучу всего и закрыть. 
# При обращении к ресурсу в нескольких местах кода, чтобы каждый раз не писать развернутую конструкцию 
# (открыть, совершить действия, обязательно закрыть, raise exceptions)

------------------------------------------------------------------------------------------------------------------------
# ТИПЫ ДАННЫХ
# 1. изменяемые - list, dict, set     
# 1. неизменяемые - str, (int, float) -> numbers, tuple, frozenset, bool

------------------------------------------------------------------------------------------------------------------------
# List - [ ] или list() состоит из строк, цифр, объектов, смеси типов, списка 

# Dict неупорядоченный набор пар ключ:значение. ключ уникальный {}

# set множество - "контейнер", содержащий не повторяющиеся элементы в случайном порядке. 
# Множества удобно использовать для удаления повторяющихся элементов

# неизменяемые аргументы в функцию передаются по значению
# изменяемые аргументы в функцию передаются по ссылкам

________________________________________________________________________________________________________________________
# venv - Виртуальное окружение (virtualenv) — это инструмент для создания отдельного пространства для проекта 
# с его зависимостями и библиотеками в директории проекта

------------------------------------------------------------------------------------------------------------------------
# self -  ссылка на экземпляр класса, первый аргумент

------------------------------------------------------------------------------------------------------------------------
# ОПП - парадигма программирования, где различные компоненты компьютерной программы моделируются на основе 
# реальных объектов. Объект — это что-либо, у чего есть какие-либо характеристики и то, 
# что может выполнить какую-либо функцию.

# Зачем нужно ООП?
# ООП используется для структурирования программы таким образом, чтобы свойства и поведения были собраны в отдельные 
# объекты. Например, в программе для управления животными в зоопарке каждое животное может быть объектом с атрибутами, 
# такими как имя, возраст и вид, а также методами, такими как кормление или игра. 
# Это делает программу легко понимаемой, расширяемой и поддерживаемой.

# ИНКАПСУЛЯЦИЯ
# Инкапсуляция просто означает скрытие данных. Как правило, в объектно-ориентированном программировании один класс 
# не должен иметь прямого доступа к данным другого класса. Вместо этого, доступ должен контролироваться через методы 
# класса. 

# НАСЛЕДОВАНИЕ
# Наследование позволяет создавать новые классы на основе уже существующих, наследуя их свойства и методы. 
# Это облегчает повторное использование кода и создание иерархий классов.

# ПОЛИМОРФИЗМ
# Термин полиморфизм буквально означает наличие нескольких форм. В контексте объектно-ориентированного программирования, 
# полиморфизм означает способность объекта вести себя по-разному.

# Полиморфизм в программировании реализуется через перегрузку метода, либо через его переопределение.

# Полиморфизм – это свойство системы использовать объекты с одинаковым интерфейсом без информации о типе и внутренней 
# структуре объекта, заключается в использовании единственной сущности(метод, оператор или объект) для представления 
# различных типов в различных сценариях использования.

# Перегрузка метода
# Перегрузка метода относится к свойству метода вести себя по-разному, в зависимости от количества или типа параметров. 
# Взглянем на очень простой пример перегрузки метода. Выполним следующий скрипт:
    class Car:  
       def start(self, a, b=None):
            if b is not None:
                print (a + b)
            else:
                print (a)

# Переопределение метода
# Переопределение метода относится к наличию метода с одинаковым названием в дочернем и родительском классах. 
# Определение метода отличается в родительском и дочернем классах, но название остается тем же. 
# Давайте посмотрим на простой пример переопределения метода в Python.
# создание класса Vehicle
    class Vehicle:  
        def print_details(self):
            print("Это родительский метод из класса Vehicle")
     
    # создание класса, который наследует Vehicle
    class Car(Vehicle):  
        def print_details(self):
            print("Это дочерний метод из класса Car")
     
    # создание класса Cycle, который наследует Vehicle
    class Cycle(Vehicle):  
        def print_details(self):    
            print("Это дочерний метод из класса Cycle")

# АБСТРАКЦИЯ
# Абстракция гласит что мы должны выделять важные характеристики объекта. Мысль в том, чтобы мы могли определить 
# минимально необходимый набор этих характеристик для того чтобы можно было решить поставленную задачу. 
# Часто путают с инкапсуляцией, потому что и то и другое косвенно влияет на формирование публичного интерфейса типа. 
# Довольно тривиальная парадигма и поэтому часто не указывается как таковая.

________________________________________________________________________________________________________________________
# ORM (Object-Relation Mapping) – общее название для фреймворков или библиотек, позволяющих автоматически связать базу 
# данных с кодом. Они стараются скрыть существование базы данных настолько, насколько это возможно. Взамен программисту 
# дают возможность оперировать данными в базе через специальный интерфейс. Вместо построения SQL-запросов, программист 
# вызывает простые методы, а всю остальную работу берёт на себя ORM.

# ORM как бы создает «виртуальную» схему базы данных в памяти и позволяет манипулировать данными уже на уровне объектов. 
# Отображение показывает как объект и его свойства связанны с одной или несколькими таблицами и их полями в базе данных.

------------------------------------------------------------------------------------------------------------------------
# SOLID
# S – Single Responsibility (Принцип единственной ответственности)
# Каждый класс должен отвечать только за одну операцию.

# O — Open-Closed (Принцип открытости-закрытости)
# Классы должны быть открыты для расширения, но закрыты для модификации.

# L — Liskov Substitution (Принцип подстановки Барбары Лисков)
# Если П является подтипом Т, то любые объекты типа Т, присутствующие в программе, могут заменяться объектами типа П 
# без негативных последствий для функциональности программы.

# I — Interface Segregation (Принцип разделения интерфейсов)
# Не следует ставить клиент в зависимость от методов, которые он не использует.

# D — Dependency Inversion (Принцип инверсии зависимостей)
# Модули верхнего уровня не должны зависеть от модулей нижнего уровня. И те, и другие должны зависеть от абстракций. 
# Абстракции не должны зависеть от деталей. Детали должны зависеть от абстракций.


# KISS
# Принцип Keep It Stupid Simple («Придерживайся простоты») велит вам следить за тем, чтобы код оставался как можно более
# простым. Чем код проще, тем легче в нем разобраться, как вам, так и другим людям, занимающимся его поддержкой. 
# Под простотой главным образом имеется в виду отказ от использования хитроумных приемов и ненужного усложнения.
# В качестве примеров нарушения этого принципа можно назвать написание отдельной функции только лишь для осуществления 
# операции сложения или использование побитового оператора (right shift >> 1) для деления целых чисел на 2. Последнее, 
# безусловно, более эффективно, чем обычное (/2), но при этом очень сильно снижается понятность кода. 
# Применяя такой подход, вы осуществляете clever coding («заумный кодинг») и over-optimization (чрезмерную оптимизацию).
# И то, и другое в долгосрочной перспективе не слишком хорошо сказывается на здоровье вашего кода.

# DRY
# Принцип Don’t Repeat Yourself («Не повторяйся») напоминает нам, что каждое повторяемое поведение в коде следует 
# обособлять (например, выделять в отдельную функцию) для возможности многократного использования. Когда у вас в 
# кодовой базе есть два совершенно одинаковых фрагмента кода, это не хорошо. Это часто приводит к рассинхронизации и 
# прочим багам, не говоря уже о том, что от этого увеличивается размер программы.

# YAGNI
# Принцип You Aren’t Gonna Need It («Тебе это не понадобится») говорит о том, что нежелательно оставлять в продакшене 
# «точки расширения» (места, предназначенные только для того, чтобы позволить вам в будущем легко добавить новый 
# функционал). Конечно, мы не говорим о случаях, когда речь идет об уже заказанном функционале. Такие точки расширения 
# вносят ненужную сложность и увеличивают размер вашей кодовой базы.

# SLAP
# Принцип Single Level of Abstraction Principle («Принцип единого уровня абстракций») означает, что функции должны 
# иметь единый уровень абстракции. Скажем, функция, читающая input, не должна также обрабатывать полученные данные. 
# Для этого она должна задействовать отдельную функцию, находящуюся на другом, более низком уровне абстракции. 
# Чем более общей является функция и чем больше других функций она использует, тем выше она располагается в 
# абстракционной иерархии.

------------------------------------------------------------------------------------------------------------------------
# ПАТЕЕРНЫ

# Порождающие (Creational)
# Порождающие паттерны проектирования описывают, как создавать объекты. Обычно объект создается путем вызова 
# констуктора, но иногда требуется большая гибкость именно для этого порождающие паттерны и полезны.

# Абстрактная фабрика (Abstract factory)
# Предназначен для случаев, когда требуется создать сложный объект, состоящий из других объектов, причем все 
# составляющие объекты принадлежат одному "семейству". Предоставляет интерфейс для создания семейств взаимосвязанных 
# или взаимозависимых объектов, не специфицируя их конкретных классов.
# Например, в системе с GUI может быть абстрактная фабрика виджетов, которой наследуют три конкретных фабрики: 
# MacWidgetFactory, XfceWidgetFactory, WindowsWidgetFactory, каждая из которых предоставляет методы для создания 
# одних и тех же объектов (make_button(), make_spinbox() и т.д), стилизованных, однако, как принято на конкретной 
# платформе. Это дает возможность создать обобщенную функцию create_dialog(), которая принимает экземпляр фабрики в 
# качестве аргумента и создает диалоговое окно, выглядещее как в OS X, Xfce или Windows - в зависимости от того какую 
# фабрику мы передали.

# Построитель (Builder)
# Построитель аналогичен паттерну Абстрактная фабрика в том смысле, что оба предназначены для создания сложных объектов,
# составленных из других объектов. Но отличается тем, что не только предоставляет методы для построения сложного 
# объекта, но и хранит внутри себя его полное представление.
# Этот паттерн допускает такую же композиционную структуру как и Абстрактная фабрика (то есть сложные объекты, 
# составленные из нескольких более простых) но особенно удобен в ситуациях, когда представление составного объета 
# должно быть отделено от алгоритмов композиции
# Отделяет конструирование сложного объекта от его представления, так что в результате одного и того же процесса 
# конструирования могут получаться разные представления. От абстрактной фабрики отличается тем, что делает акцент на 
# пошаговом конструировании объекта. Строитель возвращает объект на последнем шаге, тогда как абстрактная фабрика 
# возвращает объект немедленно. Строитель часто используется для создания паттерна компоновщик.
# **********************************************************************************************************************

# Структурные (Structural)
# Структурные паттерны описывают, как из одних объектов составляются другие, более крупные. Рассматриваются три 
# основных круга вопросов: адаптация интерфейсов, добавление функциональности и работа с коллекциями объектов.

# Адаптер (Adapter)
# Паттерн Адаптер описывает технику адаптации интерфейса. Задача состоит в том, чтобы один класс мог воспользоваться 
# другим - с несовместимым интерфейсом - без внесения каких-либо изменений в оба класса. Это полезно, например, когда 
# требуется воспользоваться не подлежащим изменению классом в контексте, на который он не был расчитан.
# Адаптер обеспечивает совместную работу классов с несовместимыми интерфейсами, которая без него была бы невозможна.
# **********************************************************************************************************************

# Поведенческие (Behavioral)
# Предмет поведенческих паттерном - способ решения задачи, то есть они имеют дело с алгоритмами и взаимодействиями 
# объектов. Эти паттерны предлагают действенные способы обдумывания и организации вычислений. Для некоторых из них 
# имеется прямяая поддержка в синтаксисе Python.
# Цепочка ответственности (Chain of responsibility)
# Паттерн цепочка отвестственности предназначен, для того чтобы разорвать связь между отправителем запроса и 
# получателем, который этот запрос обрабатывает. Вместо непосредственного вызова одной функции из другой первая функция
# отправляет запрос цепочке получателей. Первый получатель в цепочке может либо обработать запрос и прервать цепочку 
# (не передавая запрос дальше), либо передать запрос следующему получателю. У второго получателя есть такой же выбор и 
# так далее, пока запрос не дойдет до последнего получателя (который может отбросить запрос или возбудить исключение).
# Представьте себе пользовательский интерфейс, который получает события для обработки. Одни события поступают от 
# пользователя (например, события мыши и клавиатуры), другие - от системы (например, события таймера).

------------------------------------------------------------------------------------------------------------------------
# Python Global Interpreter Lock (GIL)
# Это своеобразная блокировка, позволяющая только одному потоку управлять интерпретатором Python. 
# Это означает, что в любой момент времени будет выполняться только один конкретный поток.  
# Потоки используют одну и ту же выделенную память. Когда несколько потоков работают одновременно, то нельзя угадать 
# порядок, в котором потоки будут обращаться к общим данным. Результат доступа к совместно используемым данным 
# зависит от алгоритма планирования. который решает, какой поток и когда запускать. Если такого алгоритма нет, 
# то конечные данные могут быть не такими как ожидаешь.
# Без алгоритмов планирования доступа потоков к общим данным такие ошибки очень трудно найти и произвести отладку. 
# Кроме того, они, как правило, происходят случайным образом, вызывая беспорядочное и непредсказуемое поведение.
# Есть еще худший вариант развития событий, который может произойти без встроенной в Python блокировки потоков GIL. 
# Например, если оба потока начинают читать глобальную переменную a одновременно

------------------------------------------------------------------------------------------------------------------------
# ПАРАЛЛЕЛИЗМ
# Используя многопоточность threading, позволяя нескольким потокам работать по очереди.

# Используя несколько ядер процессора multiprocessing. Делать сразу несколько вычислений, используя несколько 
# ядер процессора. Это и называется параллелизмом.

# Используя асинхронный ввод-вывод с модулем asyncio. Запуская какую то задачу, продолжать делать другие вычисления, 
# вместо ожидания ответа от сетевого подключения или от операций чтения/записи

------------------------------------------------------------------------------------------------------------------------
# Exceprions — это тип данных, который нужен для того, что бы сообщать нам об ошибках. Существует базовое исключение 
# BaseException от которого наследуются все остальные исключения. В блоке try мы выполняем инструкцию, которая может 
# породить исключение, а в блоке except мы ловим ошибки и делаем свои операции. Стоит учесть, что мы можем делать 
# бесконечное количество вложенных блоков. Грамотным способом является вылавливать только те 
# исключения, которые мы ожидаем.

------------------------------------------------------------------------------------------------------------------------
# Хэш-функция - это функция, которая принимает на вход какие-либо данные (например, строки) и возвращает число по 
# некоторому заданному алгоритму.  Если эта функция является идеальной - то для каждого переданного на вход функции 
# значения будет возвращено число, отличное от ранее полученных. В противном случае, будут возникать коллизии, 
# когда для различных входных данных возвращается одно и то же число. Назначением хэш-функций является возможность 
# помещения некоторого элемента (например, строки) в хэш-таблицу, на основе которых реализованы, 
# например, словари и множества в Python.

------------------------------------------------------------------------------------------------------------------------
# Python — высокоуровневый язык программирования общего назначения с динамической строгой типизацией и автоматическим 
# управлением памятью, ориентированный на повышение производительности разработчика, читаемости кода и его качества, 
# а также на обеспечение переносимости написанных на нём программ. Язык является полностью объектно-ориентированным в 
# том плане, что всё является объектами. Необычной особенностью языка является выделение блоков кода отступами. 
# Синтаксис ядра языка минималистичен, за счёт чего на практике редко возникает необходимость обращаться к 
# документации. Сам же язык известен как интерпретируемый и используется, в том числе для написания скриптов. 
# Недостатками языка являются зачастую более низкая скорость работы и более высокое потребление памяти написанных на 
# нём программ по сравнению с аналогичным кодом, написанным на компилируемых языках, таких как C или C++

# Python является интерпретируемым языком программирования, но утверждать, что он полностью интерпретируемый, 
# не совсем верно, поскольку есть некоторые аспекты компиляции.

# Процесс выполнения программы обычно выглядит следующим образом:

# 1️⃣ Интерпретация и компиляция: 
# Исходный код сначала проходит через процесс компиляции в промежуточный байт-код. Это выполняется интерпретатором 
# при запуске программы. В результате компиляции создается файл .pyc, который содержит байт-код программы.

# 2️⃣ Исполнение: 
# Затем интерпретатор исполняет этот байт-код последовательно, инструкция за инструкцией. Во время выполнения 
# интерпретатор обрабатывает и выполняет инструкции, предоставляя ожидаемый результат.

# Python является интерпретируемым языком с компиляцией в промежуточный байт-код, который затем интерпретируется и 
# выполняется. Этот подход сочетает в себе преимущества интерпретации (гибкость, динамическая типизация) с некоторыми 
# преимуществами компиляции (более быстрое выполнение благодаря использованию байт-кода).

# Однако стоит отметить, что существуют и другие реализации Python, такие, как PyPy, которые используют JIT 
# (Just-In-Time) компиляцию для более эффективного выполнения кода. Каждая реализация может иметь свои особенности и 
# характеристики в этом отношении.


# install black
```shell
pip install black
```

# check code with [black]
```shell
black .
```
"""
1. What is Python? List some popular applications of Python in the world of technology.
Python is a widely-used general-purpose, high-level programming language. It was created by Guido van Rossum in 1991
and further developed by the Python Software Foundation. It was designed with an emphasis on code readability,
and its syntax allows programmers to express their concepts in fewer lines of code.
It is used for:

- System Scripting
- Web Development
- Game Development
- Software Development
- Complex Mathematics

1. Что такое Питон? Перечислите некоторые популярные приложения Python в мире технологий.
Python — широко используемый язык программирования высокого уровня общего назначения.
Он был создан Гвидо ван Россумом в 1991 году и далее развит Python Software Foundation.
Он был разработан с упором на читаемость кода, а его синтаксис позволяет программистам
выражать свои концепции в меньшем количестве строк кода.
Он используется для:

- Системные сценарии
- Веб-разработка
- Разработка игр
- Разработка программного обеспечения
- Сложная математика

2. What are the benefits of using Python language as a tool in the present scenario?
The following are the benefits of using Python language:

- Object-Oriented Language
- High-Level Language
- Dynamically Typed language
- Extensive support Libraries
- Presence of third-party modules
- Open source and community development
- Portable and Interactive
- Portable across Operating systems

3. Is Python a compiled language or an interpreted language?
Actually, Python is a partially compiled language and partially interpreted language.
The compilation part is done first when we execute our code and this will generate byte code internally this byte
code gets converted by the Python virtual machine(p.v.m) according to the underlying platform(machine+operating system).

4. What does the ‘#’ symbol do in Python?
‘#’ is used to comment on everything that comes after on the line.

5. What is the difference between a Mutable datatype and an Immutable data type?
Mutable data types can be edited i.e., they can change at runtime. Eg – List, Dictionary, etc.
Immutable data types can not be edited i.e., they can not change at runtime. Eg – String, Tuple, etc.

6. What is the difference between a Set and Dictionary?
The set is an unordered collection of data types that is iterable, mutable and has no duplicate elements.
A dictionary in Python is an ordered collection of data values, used to store data values like a map.

7. What is List Comprehension? Give an Example.
List comprehension_and_generators is a syntax construction to ease the creation of a list based on existing iterable.

For Example:
my_list = [i for i in range(1, 10)]

8. What is a lambda function?
A lambda function is an anonymous function. This function can have any number of parameters but,
can have just one statement. For Example:

a = lambda x, y : x*y
print(a(7, 19))

9. What is a pass in Python?
Pass means performing no operation or in other words, it is a placeholder in the compound statement,
where there should be a blank left and nothing has to be written there.

10. What is the difference between / and // in Python?
/ represents precise division (result is a floating point number) whereas
// represents floor division (result is an integer).

For Example:

5//2 = 2
5/2 = 2.5

11. How is Exceptional handling done in Python?
There are 3 main keywords i.e. try, except, and finally which are used to catch exceptions and handle the recovering
mechanism accordingly. Try is the block of a code that is monitored for errors.
Except block gets executed when an error occurs.

The beauty of the final block is to execute the code after trying for an error.
This block gets executed irrespective of whether an error occurred or not.
Finally, block is used to do the required cleanup activities of objects/variables.

12. What is swapcase function in Python?
It is a string’s function that converts all uppercase characters into lowercase and vice versa.
It is used to alter the existing case of the string. This method creates a copy of the string which contains
all the characters in the swap case. For Example:

string = "GeeksforGeeks"
string.swapcase() ---> "gEEKSFORgEEKS"

13. Difference between for loop and while loop in Python
The “for” Loop is generally used to iterate through the elements of various collection types such as
List, Tuple, Set, and Dictionary. Developers use a “for” loop where they have both the conditions start and the end.
Whereas, the “while” loop is the actual looping feature that is used in any other programming language.
Programmers use a Python while loop where they just have the end conditions.

14. Can we Pass a function as an argument in Python?
Yes, Several arguments can be passed to a function, including objects, variables (of the same or distinct data types),
and functions. Functions can be passed as parameters to other functions because they are objects.
Higher-order functions are functions that can take other functions as arguments.

15. What are *args and *kwargs?
To pass a variable number of arguments to a function in Python, use the special syntax *args and **kwargs in the
function specification. It is used to pass a variable-length, keyword-free argument list. By using the *,
the variable we associate with the * becomes iterable, allowing you to do operations on it such as iterating
over it and using higher-order operations like map and filter.

16. Is Indentation Required in Python?
Yes, indentation is required in Python. A Python interpreter can be informed that a group of statements belongs
to a specific block of code by using Python indentation. Indentations make the code easy to read for developers
in all programming languages but in Python, it is very important to indent the code in a specific order.

"""

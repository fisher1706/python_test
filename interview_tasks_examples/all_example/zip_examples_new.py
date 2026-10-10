"""
Demonstration of Python's zip() function.
"""

# Simple example
names = ["Анна", "Борис", "Виктор"]
ages = [20, 25, 30]

result = zip(names, ages)
print("Simple example:")
print(list(result))
print()

# Using zip() in a loop
print("Loop example:")
for name, age in zip(names, ages):
    print(f"{name}: {age}")
print()

# Different lengths
a = [1, 2, 3, 4]
b = ["a", "b"]

print("Different lengths:")
print(list(zip(a, b)))
print()

# Three sequences
cities = ["Москва", "Казань", "Сочи"]

print("Three sequences:")
for name, age, city in zip(names, ages, cities):
    print(name, age, city)
print()

# Unpacking
pairs = [
    ("Анна", 20),
    ("Борис", 25),
    ("Виктор", 30),
]

names2, ages2 = zip(*pairs)

print("Unpacking:")
print(names2)
print(ages2)
print()

# Dictionary creation
keys = ["name", "age", "city"]
values = ["Анна", 20, "Москва"]

person = dict(zip(keys, values))

print("Dictionary:")
print(person)
print()

# zip returns an iterator
z = zip([1, 2], [3, 4])

print("zip object:")
print(z)
print("As a list:")
print(list(z))

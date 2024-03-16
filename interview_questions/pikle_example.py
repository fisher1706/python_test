"""
Модуль pickle дозволяє зберігати у файлах будь-які об’єкти Python без використання зайвих перетворень. В цілому,
модуль pickle реалізує двійковий протокол для серіалізації та десеріалізації об’єктів. Під серіалізацією розуміється
перетворення об’єктів в рядок байт.
Десеріалізація передбачає зворотну операцію конвертування потоку байт у вихідний об’єкт.

dumps() - претрорюємо в байт
loads() - претрорюємо в об’єкт
"""

import pickle


# initializing data to be stored in db
Omkar = {
    'key': 'Omkar',
    'name': 'Omkar Pathak',
    'age': 21,
    'pay': 40000
}

Jagdish = {
    'key': 'Jagdish',
    'name': 'Jagdish Pathak',
    'age': 50,
    'pay': 50000
}

# database
db = {
    'Omkar': Omkar,
    'Jagdish': Jagdish
}


if __name__ == '__main__':
    # For storing
    # type(b) gives <class 'bytes'>;
    b = pickle.dumps(db)
    print(f"b:= {b}")
    print("*" * 200)

    # For loading
    myEntry = pickle.loads(b)
    print(myEntry)

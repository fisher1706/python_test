"""
Контекстный менеджер в Python - это специальный тип объекта,
который предназначен для управления контекстом в блоке кода.
Основная цель контекстного менеджера - обеспечить корректное управление ресурсами,
такими как файлы, сетевые соединения или блокировки в многопоточных программах.
Это помогает предотвратить ошибки, такие как утечки ресурсов, и делает код более читаемым и безопасным.
Чтобы понять, как работает контекстный менеджер, рассмотрим два ключевых метода, которые он должен реализовывать:
enter и exit.

Метод __enter__() вызывается в начале блока кода, управляемого контекстным менеджером
(обычно после ключевого слова with), и обычно используется для выделения ресурсов.

Метод __exit__() вызывается после окончания блока кода и обычно занимается очисткой ресурсов.

В этом примере FileHandler - это контекстный менеджер для работы с файлами.
Когда начинается блок with, вызывается метод __enter__(), который открывает файл.
После завершения работы в блоке with автоматически вызывается метод __exit__(), который закрывает файл.
Это предотвращает ошибки, связанные с забытым закрытием файла, и делает код более надежным и читаемым.
Контекстные менеджеры широко используются в Python для управления ресурсами, их можно встретить в стандартной
библиотеке (например, open для файлов), а также во многих сторонних библиотеках.

Кратко: Контекстный менеджер в Python - это способ управления ресурсами в блоке кода,
обеспечивающий автоматическое выделение и освобождение ресурсов.
"""


class FileHandler:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()


if __name__ == "__main__":
    # Использование контекстного менеджера
    with FileHandler("example.txt", "w") as f:
        f.write("Привет, мир!")

    # После выхода из блока with файл автоматически закрывается

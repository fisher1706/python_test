"""
Use the with statement to manage resources.
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


from contextlib import contextmanager


@contextmanager
def managed_resource():
    print("Acquiring resource")
    yield "Resource"
    print("Releasing resource")


if __name__ == "__main__":
    with FileHandler("example.txt", "w") as f:
        f.write("Привет, мир!")

    print("*" * 200)

    with managed_resource() as resource:
        print(f"Using {resource}")

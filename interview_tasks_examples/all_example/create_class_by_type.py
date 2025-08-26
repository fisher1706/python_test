# Dynamically create a class named 'Student' with no base classes and an attribute 'subject'
Student = type(
        'Student',
        (),
        {'subject': 'Math'}
    )


if __name__ == '__main__':
    # Print the type of the created class
    print(type(Student))  # Output: <class 'type'>

    # Print the name of the created class
    print(Student.__name__)  # Output: Student

    # Print the attributes of the created class
    print(Student.__dict__)  # Output: {'__module__': '__main__', '__qualname__': 'Student', 'subject': 'Math'}

    # Usage
    student_instance = Student()
    print(student_instance.subject)  # Output: Math

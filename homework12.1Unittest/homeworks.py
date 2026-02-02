class Student:
    def __init__(self, name, surname, age, average_grade):
        self.name = name
        self.surname = surname
        self.age = age
        self.average_grade = average_grade

    def change_grade(self, new_grade):
        self.average_grade = new_grade


def unique_char_count(text: str) -> int:
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    return len(set(text))


def has_more_than_10_unique_chars(text: str) -> bool:
    return unique_char_count(text) > 10


def plus_plus(a, b):
    return a + b
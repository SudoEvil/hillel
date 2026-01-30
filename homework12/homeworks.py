# # task8
class Student:
    def __init__(self, name, surname, age, average_grade):
        self.name = name
        self.surname = surname
        self.age = age
        self.average_grade = average_grade

    def change_grade(self, new_grade):
        self.average_grade = new_grade


good_student = Student("Імʼя", "Прізвище", 17, 90)

print(
    f"Студент: {good_student.name} {good_student.surname}, "
    f"вік: {good_student.age}, "
    f"середній бал: {good_student.average_grade}"
)

good_student.change_grade(100)

print(f"Новий середній бал: {good_student.average_grade}")

#---------------------------------------------------------------

# task 7
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def plus_plus(a, b):
    return a + b

print(plus_plus(1, 2))


#---------------------------------------------------------------


def unique_char_count(text: str) -> int:
    """Повертає кількість унікальних символів у рядку."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    return len(set(text))



#---------------------------------------------------------------

def has_more_than_10_unique_chars(text: str) -> bool:
    """True, якщо унікальних символів більше 10."""
    return unique_char_count(text) > 10




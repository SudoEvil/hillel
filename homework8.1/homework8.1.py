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
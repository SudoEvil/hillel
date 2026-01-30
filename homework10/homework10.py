# Завдання 1
# Створіть клас Employee, який має атрибути name та salary.
# Далі створіть два класи, Manager та Developer, які успадковуються від Employee.
# Клас Manager повинен мати додатковий атрибут department,
# а клас Developer - атрибут programming_language.
#
# Тепер створіть клас TeamLead, який успадковується як від Manager, так і від Developer.
# Цей клас представляє керівника з команди розробників.
# Клас TeamLead повинен мати всі атрибути як Manager (ім'я, зарплата, відділ),
# а також атрибут team_size, який вказує на кількість розробників у команді, якою керує керівник.)
#
# Напишіть тест, який перевіряє наявність атрибутів з Manager та Developer у класі TeamLead
#
#
#
class Employee:
    def __init__(self, name, salary, **kwargs):
        self.name = name
        self.salary = salary
        super().__init__(**kwargs)


class Manager(Employee):
    def __init__(self, department, **kwargs):
        self.department = department
        super().__init__(**kwargs)


class Developer(Employee):
    def __init__(self, programming_language, **kwargs):
        self.programming_language = programming_language
        super().__init__(**kwargs)


class TeamLead(Manager, Developer):
    def __init__(self, name, salary, department, programming_language, team_size):
        self.team_size = team_size
        super().__init__(
            name=name,
            salary=salary,
            department=department,
            programming_language=programming_language
        )


# test
def test_teamlead_attributes():
    lead = TeamLead(
        name="Alex",
        salary=3000,
        department="IT",
        programming_language="Python",
        team_size=5
    )

    assert hasattr(lead, "name")
    assert hasattr(lead, "salary")
    assert hasattr(lead, "department")
    assert hasattr(lead, "programming_language")
    assert hasattr(lead, "team_size")

    print("✅ Test passed: all TeamLead attributes are present")


test_teamlead_attributes()


# Завдання 2
# Створіть абстрактний клас "Фігура" з абстрактними методами для отримання площі та периметру.
# Наслідуйте від нього декілька (> 2) інших фігур, та реалізуйте математично вірні для
# них методи для площі
# та периметру. Властивості по типу “довжина сторони” й т.д. повинні бути приватними,
# та ініціалізуватись через конструктор.
# Створіть Декілька різних об’єктів фігур, та у циклі порахуйте та виведіть в консоль площу та
# периметр кожної.


from abc import ABC, abstractmethod
import math


class Figure(ABC):

    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def perimeter(self) -> float:
        pass


class Square(Figure):
    def __init__(self, side: float):
        self.__side = side

    def area(self) -> float:
        return self.__side ** 2

    def perimeter(self) -> float:
        return 4 * self.__side


class Rectangle(Figure):
    def __init__(self, width: float, height: float):
        self.__width = width
        self.__height = height

    def area(self) -> float:
        return self.__width * self.__height

    def perimeter(self) -> float:
        return 2 * (self.__width + self.__height)


class Circle(Figure):
    def __init__(self, radius: float):
        self.__radius = radius

    def area(self) -> float:
        return math.pi * (self.__radius ** 2)

    def perimeter(self) -> float:
        return 2 * math.pi * self.__radius


figures = [
    Square(5),
    Rectangle(3, 7),
    Circle(4),
    Square(2.5),
    Rectangle(10, 2),
]


for fig in figures:
    print(f"{fig.__class__.__name__}: area = {fig.area():.2f}, perimeter = {fig.perimeter():.2f}")


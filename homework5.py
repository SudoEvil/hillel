# Given list of tuples (name, surname, age, profession, City location)
# 1 - Add your new record o the beginning of the given list
# 2 - In modified list swap elements with indexes 1 and 5 (1<->5). Print result
# 3 - check that all people in modified list with records indexes 6, 10, 13
#   have age >=30. Print condition check result

people_records = [
  ('John', 'Doe', 28, 'Engineer', 'New York'),
  ('Alice', 'Smith', 35, 'Teacher', 'Los Angeles'),
  ('Bob', 'Johnson', 45, 'Doctor', 'Chicago'),
  ('Emily', 'Williams', 30, 'Artist', 'San Francisco'),
  ('Michael', 'Brown', 22, 'Student', 'Seattle'),
  ('Sophia', 'Davis', 40, 'Lawyer', 'Boston'),
  ('David', 'Miller', 33, 'Software Developer', 'Austin'),
  ('Olivia', 'Wilson', 27, 'Marketing Specialist', 'Denver'),
  ('Daniel', 'Taylor', 38, 'Architect', 'Portland'),
  ('Grace', 'Moore', 25, 'Graphic Designer', 'Miami'),
  ('Samuel', 'Jones', 50, 'Business Consultant', 'Atlanta'),
  ('Emma', 'Hall', 31, 'Chef', 'Dallas'),
  ('William', 'Clark', 29, 'Financial Analyst', 'Houston'),
  ('Ava', 'White', 42, 'Journalist', 'San Diego'),
  ('Ethan', 'Anderson', 36, 'Product Manager', 'Phoenix')
]


# + мій запис на початку
my_record = ("name", "surname", "age", "profession", "city")
people_records.insert(0, my_record)
print(people_records)

#У модифікованому списку обміняйте елементи з індексами 1 і 5 (1<->5). Виведіть результат.
people_records[1],  people_records[5] = people_records[5], people_records[1]
print(people_records)


#Перевірте, чи всі люди в модифікованому списку з індексами 6, 10, 13 мають вік ≥ 30. Виведіть результат перевірки
age_6 = people_records[6][2]
age_10 = people_records[10][2]
age_13 = people_records[13][2]

if (age_6 >= 30) and (age_10 >= 30) and (age_13 >= 30):
  print("У 6, 10 та 13 юзера вік ≥ 30")
else:
  print("Не всі юзери мають вік ≥ 30")


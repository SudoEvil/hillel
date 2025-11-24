# alice_in_wonderland = '"Would you tell me, please, which way I ought to go from here?"\n"That depends a good deal on where you want to get to," said the Cat.\n"I don't much care where ——" said Alice.\n"Then it doesn't matter which way you go," said the Cat.\n"—— so long as I get somewhere," Alice added as an explanation.\n"Oh, you're sure to do that," said the Cat, "if you only walk long enough."'
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк


"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
black_sea = 436402
azov_sea = 37800
area = black_sea + azov_sea
print(f"Площа Чорного та Азовського морів - " ,area, "км2")

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
all_goods = 375291
first_and_second_store = 250449
second_and_third_store = 222950


second_store = first_and_second_store + second_and_third_store - all_goods
first_store = first_and_second_store - second_store
third_store = second_and_third_store - second_store
print(f" перший склад - ", first_store, "\n", "Другий склад - ", second_store, "\n", "Третій склад - ", third_store)
# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
credit_per_month = 1179
period_credit = 18
total_sum_PC = credit_per_month * period_credit
print(f"Всього компуктер вартує ", total_sum_PC)

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
a = 8019 % 8
b = 9907 % 9
c = 2789 % 5
d = 7248 % 6
e = 7128 % 5
f = 19224 % 9
print(a, f"\n", b, "\n", c, "\n", d, "\n", e, "\n", f, "\n")

# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
quantity_pizza_big = 4
quantity_pizza_medium = 2
quantity_juice = 4
quantity_cake = 1
quantity_water = 3

price_pizza_big = 274
price_pizza_medium = 218
price_juice = 35
price_cake = 350
price_water = 21

total_pizza_big = price_pizza_big * quantity_pizza_big
total_pizza_medium = price_pizza_medium * quantity_pizza_medium
total_juice = price_juice * quantity_juice
total_cake = price_cake * quantity_cake
total_water = price_water * quantity_water

total_sum = total_pizza_big + total_pizza_medium + total_juice + total_cake + total_water
print(f"Всього до сплати за список продуктів -",total_sum)


# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
all_photos = 232
max_photo_per_page = 8
pages_need = all_photos / max_photo_per_page
print(pages_need)

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""

distance_between_cities = 1600
consumption_100km = 9
volume_gas_tank = 48
_100km = 100

section = distance_between_cities / _100km
gas_need = section * consumption_100km
stops = gas_need / volume_gas_tank
print(f"Зупинятись будем -", stops, "разів", "\n", "Загальна кількість палива -", gas_need)

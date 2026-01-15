# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while multiplier != 0:
        result = number * multiplier
        # десь тут помила, а може не одна
        if  result >= 25:
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1

#
# multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def plus_plus(a, b):
    return a + b

print(plus_plus(1, 2))

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
lst = [2, 2, 8]

def average(some_lst):
    total = sum(some_lst) / len(some_lst)
    return total

print(average(lst))


# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
some_string = "qwertyuiop"

def reverse_string(string):
    return string[::-1]

print(reverse_string(some_string))





# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
lst_words = ['cat', 'flugigenhime', 'flugigenhime']

def the_most_longer(some_lst):
    if not some_lst:
        return None
    longest_word = some_lst[0]
    for word in some_lst:
        if len(word) > len(longest_word):
            longest_word = word

    return longest_word

print(the_most_longer(lst_words))
# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):
    return str1.find(str2)

# str1 = "Hello, world!"
# str2 = "world"
# print(find_substring(str1, str2))

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2))

# task 7
# Перша книжка коштує стільки, скільки ми введемо грн., друга - на 2 грн. дороже,
# а третя - як половина вартості першої та другої разом.
# Скільки будуть коштувати усі книги, якщо купити по одному примірнику?


def give_me_total_of_books(first_book):
    second_book = first_book + 2
    third_book = (first_book + second_book) / 2
    summury = first_book + second_book + third_book
    return summury

print(give_me_total_of_books(5))





# task 8
def total_sea_area(black_sea, azov_sea):
    return black_sea + azov_sea
black_sea_area = 436_402
azov_sea_area = 37_800

result = total_sea_area(black_sea_area, azov_sea_area)
print(result)


# task 9
def warehouse_items(total, first_second, second_third):
    third = total - first_second
    second = second_third - third
    first = first_second - second
    return first, second, third

# task 10
def computer_price(monthly_payment, years):
    months = years * 12
    return months * monthly_payment
price = computer_price(1179, 1.5)
print(price)



"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""
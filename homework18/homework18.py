import logging
from functools import wraps


# Напишіть генератор, який повертає послідовність парних чисел від 0 до N.
def even_numbers_gen(n: int):
    for x in range(0, n + 1):
        if x % 2 == 0:
            yield x
print(list(even_numbers_gen(10)))

# Створіть генератор, який генерує послідовність Фібоначчі до певного числа N.
def fibonacci_up_to(n: int):
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b

print(list(fibonacci_up_to(10)))


#_____________________________________________________________________________________
# Реалізуйте ітератор для зворотного виведення елементів списку.
class ReverseListIterator:
    def __init__(self, items: list):
        self._items = items
        self._index = len(items) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < 0:
            raise StopIteration
        value = self._items[self._index]
        self._index -= 1
        return value
print(list(ReverseListIterator(list(range(10)))))


# Напишіть ітератор, який повертає всі парні числа в діапазоні від 0 до N.
class EvenRangeIterator:
    def __init__(self, n: int):
        self._n = n
        self._current = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self._current <= self._n and self._current % 2 != 0:
            self._current += 1

        if self._current > self._n:
            raise StopIteration

        value = self._current
        self._current += 1
        return value

print(list(EvenRangeIterator(10)))


#_____________________________________________________________________________________

# Напишіть декоратор, який логує аргументи та результати викликаної функції.
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

def log_args_and_result(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.info("Calling %s with args=%s kwargs=%s", func.__name__, args, kwargs)
        result = func(*args, **kwargs)
        logger.info("%s returned %r", func.__name__, result)
        return result
    return wrapper

@log_args_and_result
def add(a, b):
    return a + b
print("Decorator log args/result -> add:", add(2, 3))


# Створіть декоратор, який перехоплює та обробляє винятки, які виникають в ході виконання функції.
def handle_exceptions(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logger.exception("Error in %s: %s", func.__name__, e)
            return None
    return wrapper

@handle_exceptions
def divide(a, b):
    return a / b


print("Decorator exception handler -> divide(10, 2):", divide(10, 2))
print("Decorator exception handler -> divide(10, 0):", divide(10, 0))
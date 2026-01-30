import pytest
from homeworks import Student, unique_char_count, has_more_than_10_unique_chars, plus_plus


# ---------- Student ----------

def test_student_init_sets_attributes():
    s = Student("Імʼя", "Прізвище", 17, 90)
    assert s.name == "Імʼя"
    assert s.surname == "Прізвище"
    assert s.age == 17
    assert s.average_grade == 90


def test_student_change_grade_updates_average_grade():
    s = Student("Імʼя", "Прізвище", 17, 90)
    s.change_grade(100)
    assert s.average_grade == 100


def test_student_change_grade_allows_lower_value():
    s = Student("Імʼя", "Прізвище", 17, 90)
    s.change_grade(50)
    assert s.average_grade == 50


# ---------- unique_char_count ----------

def test_unique_char_count_basic():
    assert unique_char_count("hello") == 4  # h,e,l,o


def test_unique_char_count_empty():
    assert unique_char_count("") == 0


def test_unique_char_count_all_unique():
    assert unique_char_count("abcdef") == 6


def test_unique_char_count_repeats():
    assert unique_char_count("aaaaa") == 1


def test_unique_char_count_space_is_a_char():
    assert unique_char_count("a a") == 2  # 'a' і ' '


def test_unique_char_count_unicode():
    assert unique_char_count("привіт🙂") == len(set("привіт🙂"))


def test_unique_char_count_raises_type_error_for_non_string():
    with pytest.raises(TypeError):
        unique_char_count(123)


# ---------- has_more_than_10_unique_chars ----------

def test_has_more_than_10_unique_chars_true_for_11_unique():
    assert has_more_than_10_unique_chars("abcdefghijk") is True  # 11 унікальних


def test_has_more_than_10_unique_chars_false_for_exact_10():
    assert has_more_than_10_unique_chars("abcdefghij") is False  # рівно 10


def test_has_more_than_10_unique_chars_false_when_many_repeats():
    assert has_more_than_10_unique_chars("aaaaaaaaaaab") is False


# ---------- plus_plus ----------

def test_plus_plus_integers():
    assert plus_plus(1, 2) == 3


def test_plus_plus_negative_and_positive():
    assert plus_plus(-5, 2) == -3


def test_plus_plus_floats():
    assert plus_plus(1.5, 2.5) == 4.0


def test_plus_plus_strings_concatenation():
    assert plus_plus("QA", " ninja") == "QA ninja"

import unittest

from homeworks import Student, unique_char_count, has_more_than_10_unique_chars, plus_plus


class TestStudent(unittest.TestCase):
    def test_student_init_sets_attributes(self):
        s = Student("Імʼя", "Прізвище", 17, 90)
        self.assertEqual(s.name, "Імʼя")
        self.assertEqual(s.surname, "Прізвище")
        self.assertEqual(s.age, 17)
        self.assertEqual(s.average_grade, 90)

    def test_student_change_grade_updates_average_grade(self):
        s = Student("Імʼя", "Прізвище", 17, 90)
        s.change_grade(100)
        self.assertEqual(s.average_grade, 100)

    def test_student_change_grade_allows_lower_value(self):
        s = Student("Імʼя", "Прізвище", 17, 90)
        s.change_grade(50)
        self.assertEqual(s.average_grade, 50)


class TestUniqueCharCount(unittest.TestCase):
    def test_unique_char_count_basic(self):
        self.assertEqual(unique_char_count("hello"), 4)

    def test_unique_char_count_empty(self):
        self.assertEqual(unique_char_count(""), 0)

    def test_unique_char_count_all_unique(self):
        self.assertEqual(unique_char_count("abcdef"), 6)

    def test_unique_char_count_repeats(self):
        self.assertEqual(unique_char_count("aaaaa"), 1)

    def test_unique_char_count_space_is_a_char(self):
        # пробел — тоже символ
        self.assertEqual(unique_char_count("a a"), 2)

    def test_unique_char_count_unicode(self):
        text = "привіт🙂"
        self.assertEqual(unique_char_count(text), len(set(text)))

    def test_unique_char_count_raises_type_error_for_non_string(self):
        with self.assertRaises(TypeError):
            unique_char_count(123)


class TestHasMoreThan10UniqueChars(unittest.TestCase):
    def test_has_more_than_10_unique_chars_true_for_11_unique(self):
        self.assertTrue(has_more_than_10_unique_chars("abcdefghijk"))

    def test_has_more_than_10_unique_chars_false_for_exact_10(self):
        self.assertFalse(has_more_than_10_unique_chars("abcdefghij"))

    def test_has_more_than_10_unique_chars_false_when_many_repeats(self):
        self.assertFalse(has_more_than_10_unique_chars("aaaaaaaaaaab"))

class TestPlusPlus(unittest.TestCase):
    def test_plus_plus_integers(self):
        self.assertEqual(plus_plus(1, 2), 3)

    def test_plus_plus_negative_and_positive(self):
        self.assertEqual(plus_plus(-5, 2), -3)

    def test_plus_plus_floats(self):
        self.assertEqual(plus_plus(1.5, 2.5), 4.0)

    def test_plus_plus_strings_concatenation(self):
        self.assertEqual(plus_plus("QA", " ninja"), "QA ninja")




if __name__ == "__main__":
    unittest.main()
# Лабораторная работа № 1 по дисциплине ЛОИС
# Выполнена студенткой группы 021702 БГУИР Василёнок Анной Александровной

# Файл unittests.py является хранилищем юнит-тестов для проверки корректности работы программы.

# Задание: "проверить, является ли строка формулой сокращённого языка лоики высказываний".

import unittest

from main import is_valid, VALID_FORMULA, NOT_VALID_FORMULA


class TestIsValid(unittest.TestCase):
    def test_1(self):
        self.assertEqual(is_valid('(A->B)'), VALID_FORMULA)

    def test_2(self):
        self.assertEqual(is_valid('(1/\(A\/C))'), VALID_FORMULA)

    def test_3(self):
        self.assertEqual(is_valid('/\A\/C'), NOT_VALID_FORMULA)

    def test_4(self):
        self.assertEqual(is_valid('C->B'), NOT_VALID_FORMULA)

    def test_5(self):
        self.assertEqual(is_valid('1/\\0'), NOT_VALID_FORMULA)

    def test_6(self):
        self.assertEqual(is_valid('(!A)'), VALID_FORMULA)

    def test_7(self):
        self.assertEqual(is_valid('(!A->(C->I))'), NOT_VALID_FORMULA)

    def test_8(self):
        self.assertEqual(is_valid('((!A)->(!((A\/B)/\K)))'), VALID_FORMULA)

    def test_9(self):
        self.assertEqual(is_valid('(A->(!B))'), VALID_FORMULA)

    def test_10(self):
        self.assertEqual(is_valid('(A)'), NOT_VALID_FORMULA)

    @staticmethod
    def run_tests():
        unittest.main()

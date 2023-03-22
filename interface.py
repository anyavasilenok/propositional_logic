# Лабораторная работа № 1 по дисциплине ЛОИС
# Выполнена студенткой группы 021702 БГУИР Василёнок Анной Александровной

# Файл interface.py предназанаяен для взаимодействия с пользователем.

# Задание: "проверить, является ли строка формулой сокращённого языка лоики высказываний".

from main import is_valid
from unittests import TestIsValid


if __name__ == "__main__":
    while True:
        mode = input("Введите цифру:\n1 - ввести формулу\n2 - тесты\n3 - выход\n")
        if mode.isnumeric() is True:
            if int(mode) == 1:
                formula = str(input("Введите формулу: "))
                print(is_valid(formula))
            if int(mode) == 2:
                TestIsValid().run_tests()
            if int(mode) == 3:
                break
        else:
            pass

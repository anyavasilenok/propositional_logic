# Лабораторная работа № 1 по дисциплине ЛОИС
# Выполнена студенткой группы 021702 БГУИР Василёнок Анной Александровной

# Файл main.py предназначен для проверки, является ли введённная строка формулой логики высказываний.

# Задание: "проверить, является ли строка формулой сокращённого языка логики высказываний".

VALID_FORMULA = "Введенная строка является формулой логики высказываний."
NOT_VALID_FORMULA = "Введенная строка не является формулой логики высказываний."


ATOM = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
        'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
        'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
        'Y', 'Z', '0', '1']

OPERATIONS = ['\\/', '/\\', '!', '~', '->']
MAX_ITERATION = 20


def is_valid(formula):
    iteration = MAX_ITERATION
    result = VALID_FORMULA
    while formula not in ATOM:
        if iteration == 0:
            return NOT_VALID_FORMULA
        else:
            formula = find_unary(formula)
            formula = find_binary(formula)
            iteration -= 1
            result = VALID_FORMULA
    return result


def find_unary(formula):
    for symbol in ATOM:
        formula = formula.replace(f'(!{symbol})', 'N')
    return formula


def find_binary(formula):
    for operation in OPERATIONS:
        for symbol_1 in ATOM:
            for symbol_2 in ATOM:
                formula = formula.replace(f'({symbol_1}{operation}{symbol_2})', 'N')
    return formula


'''Друге завдання'''
import re
from typing import Callable

def generator_numbers(text: str):
    '''function'''
    pattern = r'\b[0-9]*\.?[0-9]+\b' # Регулярний вираз для визначення дійсних чисел
    for match in re.finditer(pattern, text):
        yield float(match.group())

def sum_profit(text: str, func: Callable):
    '''function'''
    numbers_generator = func(text)
    return sum(numbers_generator)

TEXT = '''Загальний дохід працівника складається з декількох частин:
    1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів.'''
total_income = sum_profit(TEXT, generator_numbers)
print(f'Загальний дохід: {total_income}')

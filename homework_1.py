# Практическое задание 1
from _decimal import getcontext, Decimal

print('Вычислить число π c заданной точностью d')


def get_precision(number):
    s = str(number).split('.')
    return len(s[1])


# Bailey–Borwein–Plouffe formula
def calc_pi(nbm_precision):
    getcontext().prec = nbm_precision + 1
    sum_pi = 0
    for i in range(nbm_precision):
        sum_pi += (
            1 / Decimal(16)**i *
            (
                Decimal(4) / (8 * i + 1) -
                Decimal(2) / (8 * i + 4) -
                Decimal(1) / (8 * i + 5) -
                Decimal(1) / (8 * i + 6)
            )
        )
    return sum_pi


while True:
    try:
        input_number = input('Введите точность числа: ')
        float_number = float(input_number)
        if float_number < 0 or float_number > 1:
            raise ValueError
        number_precision = get_precision(input_number)
        print(f'$d = {input_number}, π = {calc_pi(number_precision)}')
        break
    except ValueError:
        print('Допустимые значения: любое вещественное число от 0 до 1')

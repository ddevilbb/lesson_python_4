# Практическое задание 4
from random import randint

print('Задана натуральная степень k. '
      'Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена '
      'и записать в файл многочлен степени k.')


while True:
    try:
        k = int(input('Введите натуральную степерь k: '))
        if k < 1:
            raise ValueError
        polynomial = ''
        for i in range(k, -1, -1):
            rnd = randint(0, 100)
            if rnd == 0:
                continue
            polynomial += (' + ' if len(polynomial) > 0 else '') + (f'{rnd}' if rnd > 1 or i == 0 else '')
            if i > 1:
                polynomial += ('*' if rnd > 1 else '') + f'x^{i}'
            elif i == 1:
                polynomial += ('*' if rnd > 1 else '') + 'x'
        polynomial += ' = 0'
        print(polynomial)
        with open('file.txt', 'a+') as f:
            f.write(f'{polynomial}\n')
            f.close()
        break
    except ValueError:
        print('Допустимые значения: любое натуральные числа от 1 до ∞')

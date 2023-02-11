# Практическое задание 5

print('Даны два файла, в каждом из которых находится запись многочлена. '
      'Задача - сформировать файл, содержащий сумму многочленов.')


def get_polynomial_from_file(filename):
    with open(filename, 'r') as f:
        file_string = (
            f.readline()
            .rstrip('\n')
            .replace('= 0', '')
            .replace(' ', '')
            .replace('+', '|+')
            .replace('-', '|-')
        )
        f.close()
        return file_string


while True:
    try:
        polynomial1 = get_polynomial_from_file('file_1.txt')
        polynomial2 = get_polynomial_from_file('file_2.txt')

        lst1 = polynomial1.split('|')
        lst2 = polynomial2.split('|')

        lst1 = [i.split('*') for i in lst1]
        lst2 = [i.split('*') for i in lst2]

        dct1 = {
            (
                (
                    int(i[1].split('^')[1]) if 1 < len(i[1].split('^')) else 1
                ) if 1 <= (len(i)-1) else 0
            ): int(i[0])
            for i in lst1
        }
        dct2 = {
            (
                (
                    int(i[1].split('^')[1]) if 1 < len(i[1].split('^')) else 1
                ) if 1 <= len(i)-1 else 0
            ): int(i[0])
            for i in lst2
        }

        res_dct = {i: (dct1[i] if i in dct1 else dct2[i]) for i in (dct2.keys() ^ dct1.keys())}

        polynomial = ''

        for i in dct1:
            if i in res_dct:
                continue
            res_dct[i] = dct1[i] + dct2[i]

        res_dct_keys = list(res_dct.keys())
        res_dct_keys.sort()
        res_dct_keys.reverse()
        res_dct = {i: res_dct[i] for i in res_dct_keys}

        for i in res_dct:
            if res_dct[i] == 0:
                continue
            polynomial += ((' + ' if res_dct[i] > 0 else ' - ') if len(polynomial) > 0 else '') + (f'{abs(res_dct[i])}' if (res_dct[i] != 1 or i == 0) else '')
            if i > 1:
                polynomial += ('*' if res_dct[i] > 1 else '') + f'x^{i}'
            elif i == 1:
                polynomial += ('*' if res_dct[i] > 1 else '') + 'x'
        polynomial += ' = 0'

        print(polynomial)
        with open('file_result.txt', 'w+') as f:
            f.write(f'{polynomial}\n')
            f.close()
        break
    except ValueError:
        print('Допустимые значения: любое натуральные числа от 1 до ∞')

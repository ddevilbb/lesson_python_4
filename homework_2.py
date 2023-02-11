# Практическое задание 2

print('Задайте натуральное число N. '
      'Напишите программу, которая составит список простых множителей числа N.')


while True:
    try:
        input_number = input('Введите натуральное число: ')
        int_number = int(input_number)
        if int_number < 1:
            raise ValueError
        result = []
        i = 2
        while i <= int_number:
            if int_number % i == 0:
                if i not in result:
                    result.append(i)
                int_number //= i
                i = 2
            else:
                i += 1
        print(f'Список простых множителей числа {input_number}: {result}')
        break
    except ValueError:
        print('Допустимые значения: любое натуральное число от 1 до ∞')

with open('num_text.txt', 'w+') as f_in:
    f_in.write(input('Введите числа через пробел: '))
    f_in.seek(0)
    for line in f_in:
        line = line.split()
        s = 0
        for i in line:
            i = int(i)
            s += i
        print(f'Сумма чисел файла {s}')



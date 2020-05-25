import json

with open('firm.txt', 'r', encoding='utf8') as f_in:
    g_list = []  # учитываем прибыльные фирмы
    list_1 = []  # учитываем убыточные фирмы
    al_list = []  # сюда переносим словарь с фирмой и результатом

    for line in f_in:
        # выделяем цифры в каждой строке
        numb = [int(num) for num in line.split() if num.isdigit()]
        res = numb[0] - numb[1]
        line = line.split()
        # вычисление прибыли и отправка в соответствующие счетчики
        if res > 0:
            g_list.append(res)
            al_list.append({res, line[0]})
        else:
            list_1.append(res)
            al_list.append({res, line[0]})

    a = num_lines = sum(1 for line in open('firm.txt'))# узнаем количество фирм

    #считаем общую сумму прибыльных предприятий
    s = 0
    for i in g_list:
        i = int(i)
        s += i

    #считаем среднюю прибыль
    aver = s / a
    d_aver = {'average_profit': aver}
    result = (f'{al_list}, {d_aver}')

    #сохраняем в виде json-объекта
    with open('John.json', 'w') as f:
        json.dump(result, f)





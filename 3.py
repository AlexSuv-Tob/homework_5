with open('staff_file.txt') as f:
    d = {}
    res = []

    for line in f:
       key, value = line.split()
       d[key] = value
       res.append(int(value))
       if int(value) < 20000:
            #print(int(value))
        print(f'{key}: зарплата меньше 20 000')
    num = int(len(d))
    aver = sum(res) / num
    print(f'{aver}: средняя зарплат по предприятию')



with open('my_let.txt', 'r', encoding='utf8') as f_in:
    for line in f_in:
        numb = [int(num) for num in line.split() if num.isdigit()]
        s = 0
        for i in numb:
            s += i
        line = line.split()
        d = {line[0]:s}
        print(d)






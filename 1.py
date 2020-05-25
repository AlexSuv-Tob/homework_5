f_1 = open("my_file.txt", 'w')
str_list = input('Введите данные: ').split()
f_1.writelines(str_list)
f_1.close()

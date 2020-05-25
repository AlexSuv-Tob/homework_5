with open('my_text.txt') as f_in, \
        open('new_text.txt', 'w', encoding='utf8') as f_out:
    for line in f_in:
        line = line.replace('One', 'Один')
        line = line.replace('Two', 'Два')
        line = line.replace('Three', 'Три')
        line = line.replace('Four', 'Четыре')
        f_out.write(line)
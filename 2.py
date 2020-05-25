f_name = 'my_next.txt'

num_lines = 0
num_words = 0

with open(f_name, 'r') as f:
    for line in f:
        words = line.split()
        num_lines += 1
        for words in line:
            num_words += len(words)


print(num_lines)
print(num_words)
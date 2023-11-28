f = open("input.txt", "r")
lines = f.readlines()

n_correct_passwords = 0
for line in lines:
    line_splitted = line.split()
    min_max = line_splitted[0].split('-')
    min = int(min_max[0])
    max = int(min_max[1])
    char = line_splitted[1][0]
    password = line_splitted[2]
    if password.count(char) >= min and password.count(char) <= max:
        n_correct_passwords = n_correct_passwords + 1

print(n_correct_passwords)

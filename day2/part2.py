f = open("input.txt", "r")
lines = f.readlines()

n_correct_passwords = 0
for line in lines:
    line_splitted = line.split()
    min_max = line_splitted[0].split('-')
    position_1 = int(min_max[0]) - 1
    position_2 = int(min_max[1]) - 1
    char = line_splitted[1][0]
    password = line_splitted[2]
    if (password[position_1] == char and password[position_2] != char or
        password[position_1] != char and password[position_2] == char):
        n_correct_passwords = n_correct_passwords + 1

print(n_correct_passwords)

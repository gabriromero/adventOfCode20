f = open("input.txt", "r")
input_lines = f.readlines()

lines = []
for input_line in input_lines:
    lines.append(str(input_line.strip()))

lines = lines[1:]
sum = 0
y = 0
for line in lines:
    y = y + 3 - 31 if y + 3 >= 31 else y + 3
    if line[y] == "#":
        sum = sum + 1
    
print(sum)
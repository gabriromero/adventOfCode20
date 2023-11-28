f = open("input.txt", "r")
lines = f.readlines()

numbers = []
for line in lines:
    numbers.append(int(line))

for x in range(len(numbers)):
    for y in range(x):
        if numbers[x] + numbers[y] == 2020:
            print(numbers[x] * numbers[y])

f = open("input.txt", "r")
lines = f.readlines()

numbers = []
for line in lines:
    numbers.append(int(line))

numbers_len = len(numbers)
for x in range(numbers_len):
    for y in range(x):
        for z in range(y):
            if numbers[x] + numbers[y] + numbers[z] == 2020:
                print(numbers[x] * numbers[y] * numbers[z])

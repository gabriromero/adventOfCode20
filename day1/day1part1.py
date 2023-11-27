f = open("input.txt", "r")

numbers = []
for x in f:
    numbers.append(f.readline())

for x in range(50):
    for y in range(x):
        if int(numbers[x]) + int(numbers[y]) == 2020:
            print(int(numbers[x]) * int(numbers[y]))

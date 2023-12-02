f = open("input.txt", "r")
input_lines = f.readlines()

lines = []
for input_line in input_lines:
    lines.append(str(input_line.strip()))

slopes = {
    "slope1": {
        'move': 1,
        'y': 0,
        'sum': 0
    },
    "slope2": {
        'move': 3,
        'y': 0,
        'sum': 0
    },
    "slope3": {
        'move': 5,
        'y': 0,
        'sum': 0
    },
    "slope4": {
        'move': 7,
        'y': 0,
        'sum': 0
    },
    "slope5": {
        'move': 1,
        'y': 0,
        'sum': 0
    }
}

for index, line in enumerate(lines):
    if index == 0:
        continue
    
    for slope in slopes:
        if index % 2 != 0 and slope == "slope5":
            continue

        slopes[slope]["y"] = (
            slopes[slope]["y"] + slopes[slope]["move"] - 31 
            if slopes[slope]["y"] + slopes[slope]["move"] >= 31 
            else slopes[slope]["y"] + slopes[slope]["move"]
        )

        if line[slopes[slope]["y"]] == "#":
            slopes[slope]["sum"] = slopes[slope]["sum"] + 1
    
    
sums = [x['sum'] for x in list(slopes.values())]
print(sums)
multiplier = 1
for sum in sums:
    multiplier = multiplier * sum
print(multiplier)
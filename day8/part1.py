file = open("input.txt", "r")

instructions = file.readline().strip()
file.readline()

maps = {}
for line in file.readlines():
    key, valueRaw = line.split("=")
    key = key.strip()
    
    value = valueRaw.strip().split(",")
    left = value[0].strip("(")
    right = value[1].strip(")").strip()

    maps[key] = [left, right]

found = False
count = 0
currKey = "AAA"
while not found:
    for char in instructions:
        if char == "R":
            currKey = maps[currKey][1]
        else:
            currKey = maps[currKey][0]
        count += 1

        if currKey == "ZZZ":
            found = True
            break

print(count)
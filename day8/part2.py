from functools import reduce
def test(nums):
    return reduce(lambda x,y:lcm(x,y),nums)
def gcd(a, b):
    while b:
        a, b = b, a%b
    return a
def lcm(a, b):
    return a*b // gcd(a, b)

file = open("input.txt", "r")

instructions = file.readline().strip()
file.readline()

starts = []
maps = {}
for line in file.readlines():
    key, valueRaw = line.split("=")
    key = key.strip()
    
    value = valueRaw.strip().split(",")
    left = value[0].strip("(")
    right = value[1].strip(")").strip()

    maps[key] = [left, right]
    if key.endswith("A"):
        starts.append(key)

# print(starts)
foundedIdx = set()
answers = []
found = False
count = 0
while not found:
    for char in instructions:
        if char == "R":
            # print(starts)
            for i in range (len(starts)):
                if i in foundedIdx:
                    continue

                starts[i] = maps[starts[i]][1]
                if starts[i].endswith("Z"):
                     foundedIdx.add(i)
                     answers.append(count+1)
        else:
            for i in range (len(starts)):
                if i in foundedIdx:
                    continue

                starts[i] = maps[starts[i]][0]
                if starts[i].endswith("Z"):
                    foundedIdx.add(i)
                    answers.append(count+1)
        count += 1

    if len(foundedIdx) == len(starts):
        break

print(test(answers))
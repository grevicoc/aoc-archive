file = open("input.txt", "r")

input = file.readline().strip().split(",")

total = 0
for item in input:
    tempTotal = 0
    for char in item:
        tempTotal += ord(char)
        tempTotal *= 17
        tempTotal %= 256
        print(tempTotal)
    
    # print(item, tempTotal)
    total += tempTotal

print(total)
    
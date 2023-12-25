file = open("input.txt", "r")

sum = 0
for line in file.readlines():
    input = line.split(":")[1].strip("\n")
    separated = input.split("|")
    winning = separated[0]
    mine = separated[1]

    winNums = []
    for item in winning.split(" "):
        if item == "":
            continue
        num = int(item)
        winNums.append(num)

    count = 0
    for item in mine.split(" "):
        if item == "":
            continue
        num = int(item)
        if num in winNums:
            count += 1

    if count == 0:
        continue

    sum += pow(2, count-1)


print(sum)    
    # print(winNums, mineNums)
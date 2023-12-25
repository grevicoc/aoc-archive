file = open("input.txt", "r")

lenCol = len(file.readline().strip())
file.seek(0)
lenRow = len(file.readlines())

upperBound = [lenRow for i in range(lenCol)]
file.seek(0)

total = 0
currRow = lenRow
for line in file.readlines():
    currCol = 0
    for char in line.strip():
        if char == ".":
            currCol += 1
            continue

        if char == "#":
            upperBound[currCol] = currRow-1
        
        if char == "O":
            print(currRow, currCol)
            # print(upperBound[currCol])
            total += upperBound[currCol]
            upperBound[currCol] -= 1

        currCol += 1

    currRow -=1

print(total)
print(upperBound)

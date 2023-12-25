mapNum = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}
arrayNum = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

file = open("input.txt", "r")
total = 0
for line in file.readlines():
    tempString = ""
    tempNum = ""
    for char in line:
        if (ord(char) >= 48 and ord(char) <=57):
            tempNum += char
            break

        isBreak = False
        tempString += char
        for val in arrayNum:
            if tempString.find(val) != -1:
                tempNum += str(mapNum[val])
                isBreak = True
        
        if isBreak:
            break

    tempString = ""
    for i in range (len(line)-1, -1, -1):
        if (ord(line[i]) >= 48 and ord(line[i]) <=57):
            tempNum += line[i]
            break

        isBreak = False
        tempString = line[i] + tempString
        for val in arrayNum:
            if tempString.find(val) != -1:
                tempNum += str(mapNum[val])
                isBreak = True
        
        if isBreak:
            break
    print(tempNum)
    num = int(tempNum)
    total += num

print(total)    
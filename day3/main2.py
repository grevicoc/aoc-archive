file = open("input.txt", "r")

idx=0
arr = []
for line in file:
    temp = []
    if idx == 0:
        for i in range (len(line)-1+2):
            temp.append(".")
        arr.append(temp)
        temp = []
        
    temp.append(".")
    cleanLine = line.strip().replace("\n","")
    for char in cleanLine:
        temp.append(char)
    temp.append(".")
    arr.append(temp)
    idx +=1

temp = []
for i in range (len(line)-1+2):
    temp.append(".")
arr.append(temp)

lArr = len(arr)
lSubArr = len(arr[0])

for i in range (lArr):
    print(arr[i])

mapNums = {}

def buildNumber(arr, i, j):
    curr = j
    while ord(arr[i][curr]) >= 48 and ord(arr[i][curr]) <= 57:
        curr -= 1
    curr += 1
    
    num = 0
    while ord(arr[i][curr]) >= 48 and ord(arr[i][curr]) <= 57:
        num = num*10 + int(arr[i][curr])
        curr += 1
    
    key = str(i) + str(curr)
    if not key in mapNums:
        mapNums[key] = num
        return num
    
    return -999

sum = 0
for i in range(1,lArr-1,1):
    for j in range (1,lSubArr-1,1):
        if ord(arr[i][j]) == 42:
            arrNum = []

            topX, topY = i-1, j
            rightTopX, rightTopY = i-1, j+1
            rightX, rightY = i, j+1
            rightBotX, rightBotY = i+1, j+1
            botX, botY = i+1, j
            leftBotX, leftBotY = i+1, j-1
            leftX, leftY = i, j-1
            leftTopX, leftTopY = i-1, j-1

            if ord(arr[topX][topY]) >= 48 and ord(arr[topX][topY]) <= 57:
                temp = buildNumber(arr, topX, topY)
                if temp != -999:
                    arrNum.append(temp)
            if ord(arr[rightTopX][rightTopY]) >= 48 and ord(arr[rightBotX][rightTopY]) <= 57:
                temp = buildNumber(arr, rightTopX, rightTopY)
                if temp != -999:
                    arrNum.append(temp)
            if ord(arr[rightX][rightY]) >= 48 and ord(arr[rightX][rightY]) <= 57:
                temp = buildNumber(arr, rightX, rightY)
                if temp != -999:
                    arrNum.append(temp)
            if ord(arr[rightBotX][rightBotY]) >= 48 and ord(arr[rightBotX][rightBotY]) <= 57:
                temp = buildNumber(arr, rightBotX, rightBotY)
                if temp != -999:
                    arrNum.append(temp)
            if ord(arr[botX][botY]) >= 48 and ord(arr[botX][botY]) <= 57:
                temp = buildNumber(arr, botX, botY)
                if temp != -999:
                    arrNum.append(temp)
            if ord(arr[leftBotX][leftTopY]) >= 48 and ord(arr[leftBotX][leftTopY]) <= 57:
                temp = buildNumber(arr, leftBotX, leftBotY)
                if temp != -999:
                    arrNum.append(temp)
            if ord(arr[leftX][leftY]) >= 48 and ord(arr[leftX][leftY]) <= 57:
                temp = buildNumber(arr, leftX, leftY)
                if temp != -999:
                    arrNum.append(temp)
            if ord(arr[leftTopX][leftTopY]) >= 48 and ord(arr[leftTopX][leftTopY]) <= 57:
                temp = buildNumber(arr, leftTopX, leftTopY)
                if temp != -999:
                    arrNum.append(temp)
            
            print(arrNum)

            if len(arrNum) == 2:
                sum += arrNum[0] * arrNum[1]

            mapNums = {}

print(sum)

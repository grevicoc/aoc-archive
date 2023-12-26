'''
Idea:
Iterate each characters and if found digit character try to build a number from it. While creation, always check the surround, is there any symbol around it? If not and found non digit character then cancel it, if yes and found non digit character then add the number we have created to the calculation.

Complexity: O(8n) == O(n)
'''

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

# for i in range (lArr):
#     print(arr[i])

num = 0
isEligible = False
sum = 0
for i in range(1,lArr-1,1):
    if num != 0 and isEligible:
        sum += num
        isEligible = False
    num = 0
    isEligible = False
    for j in range (1,lSubArr-1,1):
        if ord(arr[i][j]) >= 48 and ord(arr[i][j]) <= 57:
            num = num*10 + int(arr[i][j])

            topX, topY = i-1, j
            if ord(arr[topX][topY]) != 46 and (ord(arr[topX][topY]) < 48 or ord(arr[topX][topY]) > 57):
                isEligible = True
                
            rightTopX, rightTopY = i-1, j+1
            if ord(arr[rightTopX][rightTopY]) != 46 and (ord(arr[rightTopX][rightTopY]) < 48 or ord(arr[rightTopX][rightTopY]) > 57):
                isEligible = True
                
            rightX, rightY = i, j+1
            if ord(arr[rightX][rightY]) != 46 and (ord(arr[rightX][rightY]) < 48 or ord(arr[rightX][rightY]) > 57):
                isEligible = True
                
            rightBotX, rightBotY = i+1, j+1
            if ord(arr[rightBotX][rightBotY]) != 46 and (ord(arr[rightBotX][rightBotY]) < 48 or ord(arr[rightBotX][rightBotY]) > 57):
                isEligible = True
                
            botX, botY = i+1, j
            if ord(arr[botX][botY]) != 46 and (ord(arr[botX][botY]) < 48 or ord(arr[botX][botY]) > 57):
                isEligible = True
                
            leftBotX, leftBotY = i+1, j-1
            if ord(arr[leftBotX][leftBotY]) != 46 and (ord(arr[leftBotX][leftBotY]) < 48 or ord(arr[leftBotX][leftBotY]) > 57):
                isEligible = True
                
            leftX, leftY = i, j-1
            if ord(arr[leftX][leftY]) != 46 and (ord(arr[leftX][leftY]) < 48 or ord(arr[leftX][leftY]) > 57):
                isEligible = True
                
            leftTopX, leftTopY = i-1, j-1
            if ord(arr[leftTopX][leftTopY]) != 46 and (ord(arr[leftTopX][leftTopY]) < 48 or ord(arr[leftTopX][leftTopY]) > 57):
                isEligible = True
        else:
            if isEligible:
                sum += num
                isEligible = False
                
            num = 0
            
if num != 0 and isEligible:
    sum += num
    isEligible = False

print(sum)

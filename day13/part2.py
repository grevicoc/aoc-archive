file = open("input.txt", "r")

patterns = []
tempPattern = []
for line in file.readlines():
    if line == "\n":
        patterns.append(tempPattern)
        tempPattern = []
        continue

    tempPattern.append(line.strip())
patterns.append(tempPattern)

sum = 0
mapOfPattern = {0: 'h 7 8', 1: 'h 12 13', 7: 'h 5 6', 8: 'h 12 13', 9: 'h 16 17', 11: 'h 13 14', 12: 'h 8 9', 13: 'h 6 7', 16: 'h 1 2', 19: 'h 12 13', 24: 'h 14 15', 25: 'h 8 9', 28: 'h 5 6', 29: 'h 3 4', 30: 'h 1 2', 33: 'h 1 2', 34: 'h 3 4', 35: 'h 4 5', 37: 'h 11 12', 41: 'h 12 13', 42: 'h 8 9', 43: 'h 15 16', 44: 'h 8 9', 45: 'h 3 4', 46: 'h 11 12', 47: 'h 12 13', 52: 'h 8 9', 55: 'h 11 12', 58: 'h 8 9', 59: 'h 16 17', 60: 'h 11 12', 63: 'h 9 10', 66: 'h 4 5', 68: 'h 2 3', 70: 'h 4 5', 74: 'h 3 4', 76: 'h 2 3', 77: 'h 9 10', 78: 'h 10 11', 79: 'h 14 15', 80: 'h 6 7', 85: 'h 6 7', 86: 'h 10 11', 87: 'h 10 11', 92: 'h 8 9', 93: 'h 12 13', 96: 'h 12 13', 97: 'h 3 4', 98: 'h 5 6', 99: 'h 2 3', 2: 'v 2 3', 3: 'v 12 13', 4: 'v 1 2', 5: 'v 5 6', 6: 'v 1 2', 10: 'v 16 17', 14: 'v 4 5', 15: 'v 10 11', 17: 'v 10 11', 18: 'v 12 13', 20: 'v 15 16', 21: 'v 6 7', 22: 'v 6 7', 23: 'v 4 5', 26: 'v 11 12', 27: 'v 15 16', 31: 'v 11 12', 32: 'v 12 13', 36: 'v 2 3', 38: 'v 3 4', 39: 'v 3 4', 40: 'v 5 6', 48: 'v 1 2', 49: 'v 1 2', 50: 'v 13 14', 51: 'v 9 10', 53: 'v 2 3', 54: 'v 4 5', 56: 'v 16 17', 57: 'v 13 14', 61: 'v 2 3', 62: 'v 6 7', 64: 'v 1 2', 65: 'v 7 8', 67: 'v 3 4', 69: 'v 1 2', 71: 'v 1 2', 72: 'v 5 6', 73: 'v 8 9', 75: 'v 10 11', 81: 'v 16 17', 82: 'v 2 3', 83: 'v 1 2', 84: 'v 7 8', 88: 'v 8 9', 89: 'v 13 14', 90: 'v 1 2', 91: 'v 10 11', 94: 'v 2 3', 95: 'v 10 11'}

def isSameHorizontal(pattern, top, bot, count):
    tempCount = 0
    for i in range (len(pattern[0])):
        if pattern[top][i] != pattern[bot][i]:
            tempCount += 1

        if tempCount + count > 1:
            return tempCount
    
    return tempCount

def isReflectHorizontal(pattern, top, bot, cntDiff):
    tempCnt = isSameHorizontal(pattern, top, bot, cntDiff)
    cntDiff += tempCnt

    if cntDiff <= 1:
        if top == 0 or bot == len(pattern)-1:
            return True
        else:
            return isReflectHorizontal(pattern, top-1, bot+1, cntDiff)
    else:
        return False

#check horizontal
idx = 0
for pattern in patterns:
    type, top, bot = mapOfPattern[idx].split(" ")

    pair = []
    for i in range(0,len(pattern)-1, 1):
        if isReflectHorizontal(pattern, i, i+1, 0):
            if type == "v":
                pair = [i+1, i+2]
                break
            
            if i+1 == int(top) and i+2 == int(bot):
                continue

            pair = [i+1, i+2]
            break
    
    if len(pair) == 0:
        idx += 1
        continue

    sum += pair[0] * 100
    print(pair, idx)
    idx += 1

def isSameVertical(pattern, left, right, count):
    tempCount = 0
    for i in range (len(pattern)):
        if pattern[i][left] != pattern[i][right]:
            tempCount += 1

        if tempCount + count > 1:
            return tempCount
    
    return tempCount

def isReflectVertical(pattern, left, right, cntDiff):
    tempCnt = isSameVertical(pattern, left, right, cntDiff)
    cntDiff += tempCnt

    if cntDiff <= 1:
        if left == 0 or right == len(pattern[0])-1:
            return True
        else:
            return isReflectVertical(pattern, left-1, right+1, cntDiff)
    else:
        return False

# check vertical
idx = 0
for pattern in patterns:
    type, left, right = mapOfPattern[idx].split(" ")

    pair = []
    for j in range (0, len(pattern[0])-1, 1):
        if isReflectVertical(pattern, j, j+1, 0):
            if type == "h":
                pair = [j+1, j+2]
                break

            if j+1 == int(left) and j+2 == int(right):
                continue

            pair = [j+1, j+2]
            break
    
    if len(pair) == 0:
        idx += 1
        continue

    sum += pair[0]
    print(pair, idx)
    idx += 1

print(sum)
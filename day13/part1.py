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
mapOfCheckedPattern = {}

def isReflectHorizontal(pattern, top, bot):
    if pattern[top] == pattern[bot]:
        if top == 0 or bot == len(pattern)-1:
            return True
        else:
            return isReflectHorizontal(pattern, top-1, bot+1)
    else:
        return False

#check horizontal
idx = 0
for pattern in patterns:
    pair = []
    for i in range(0,len(pattern)-1, 1):
        if isReflectHorizontal(pattern, i, i+1):
            pair = [i+1, i+2]
            break
    
    if len(pair) == 0:
        idx += 1
        continue
    
    sum += pair[0] * 100
    print(pair)

    mapOfCheckedPattern[idx] = f"h {pair[0]} {pair[1]}"
    idx += 1

def isSameVertical(pattern, left, right):
    for i in range (len(pattern)):
        if pattern[i][left] != pattern[i][right]:
            return False
    
    return True

def isReflectVertical(pattern, left, right):
    if isSameVertical(pattern, left, right):
        if left == 0 or right == len(pattern[0])-1:
            return True
        else:
            return isReflectVertical(pattern, left-1, right+1)
    else:
        return False

#check vertical
idx = 0
for pattern in patterns:
    if idx in mapOfCheckedPattern:
        idx += 1
        continue

    pair = []
    for j in range (0, len(pattern[0])-1, 1):
        if isReflectVertical(pattern, j, j+1):
            pair = [j+1, j+2]
            break
    
    if len(pair) == 0:
        idx += 1
        continue

    sum += pair[0]
    print(pair)

    mapOfCheckedPattern[idx] = f"v {pair[0]} {pair[1]}"
    idx += 1

print(sum)
print(mapOfCheckedPattern)
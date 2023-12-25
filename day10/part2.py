import time

file  = open("test4.txt", "r")


coord = [0,0]
i = 0
map = []
for line in file.readlines():
    if "S" in line:
        j = 0
        for char in line:
            if char == "S":
                coord = [i,j] 
            j+=1   
    i+=1      
    map.append(line.strip())

top, right, bot, left = [-1,0], [0,1], [1,0], [0,-1]
start = []

if coord[0]+top[0] >= 0:
    topChar = map[coord[0]+top[0]][coord[1]+top[1]]
    if topChar == "|" or topChar == "7" or topChar == "F":
        start.append([coord[0]+top[0], coord[1]+top[1]])

if coord[1]+right[1] < len(map[0]):
    rightChar = map[coord[0]+right[0]][coord[1]+right[1]]
    if rightChar == "-" or rightChar == "J" or rightChar == "7":
        start.append([coord[0]+right[0], coord[1]+right[1]])

if coord[0]+bot[0] < len(map):
    botChar = map[coord[0]+bot[0]][coord[1]+bot[1]]
    if botChar == "|" or botChar == "L" or botChar == "J":
        start.append([coord[0]+bot[0], coord[1]+bot[1]])

if coord[1]+left[1] >= 0:
    leftChar = map[coord[0]+left[0]][coord[1]+left[1]]
    if leftChar == "-" or leftChar == "F" or leftChar == "L":
        start.append([coord[0]+left[0], coord[1]+left[1]])

path = {}
path[f"{coord[0]}{coord[1]}"] = True

count = 1
prev1 = coord.copy()
prev2 = coord.copy()
charStart1 = map[start[0][0]][start[0][1]]
charStart2 = map[start[1][0]][start[1][1]]
while start[0][0] != start[1][0] or start[0][1] != start[1][1]:
    print(start[0])
    path[f"{start[0][0]}{start[0][1]}"] = True
    path[f"{start[1][0]}{start[1][1]}"] = True

    if charStart1 == "|":
        if prev1[0] == start[0][0]-1:
            start[0][0] += 1 
            prev1[0] += 1
        else:
            start[0][0] -= 1
            prev1[0] -= 1
    elif charStart1 == "-":
        if prev1[1] == start[0][1]-1:
            start[0][1] += 1
            prev1[1] += 1
        else:
            start[0][1] -= 1
            prev1[1] -= 1
    elif charStart1 == "L":
        if prev1[1] == start[0][1]+1:
            prev1[1] = start[0][1]
            start[0][0] -= 1
        else:
            prev1[0] = start[0][0]
            start[0][1] += 1
    elif charStart1 == "J":
        if prev1[1] == start[0][1]-1:
            prev1[1] = start[0][1]
            start[0][0] -= 1
        else:
            prev1[0] = start[0][0]
            start[0][1] -= 1
    elif charStart1 == "7":
        if prev1[1] == start[0][1]-1:
            prev1[1] = start[0][1]
            start[0][0] += 1
        else:
            prev1[0] = start[0][0]
            start[0][1] -= 1
    elif charStart1 == "F":
        if prev1[1] == start[0][1]+1:
            prev1[1] = start[0][1]
            start[0][0] += 1
        else:
            prev1[0] = start[0][0]
            start[0][1] += 1
    
    if charStart2== "|":
        if prev2[0] == start[1][0]-1:
            start[1][0] += 1 
            prev2[0] += 1
        else:
            start[1][0] -= 1
            prev2[0] -= 1
    elif charStart2== "-":
        if prev2[1] == start[1][1]-1:
            start[1][1] += 1
            prev2[1] += 1
        else:
            start[1][1] -= 1
            prev2[1] -= 1
    elif charStart2== "L":
        if prev2[1] == start[1][1]+1:
            prev2[1] = start[1][1]
            start[1][0] -= 1
        else:
            prev2[0] = start[1][0]
            start[1][1] += 1
    elif charStart2== "J":
        if prev2[1] == start[1][1]-1:
            prev2[1] = start[1][1]
            start[1][0] -= 1
        else:
            prev2[0] = start[1][0]
            start[1][1] -= 1
    elif charStart2== "7":
        if prev2[1] == start[1][1]-1:
            prev2[1] = start[1][1]
            start[1][0] += 1
        else:
            prev2[0] = start[1][0]
            start[1][1] -= 1
    elif charStart2== "F":
        if prev2[1] == start[1][1]+1:
            prev2[1] = start[1][1]
            start[1][0] += 1
        else:
            prev2[0] = start[1][0]
            start[1][1] += 1
    
    charStart1 = map[start[0][0]][start[0][1]]
    charStart2 = map[start[1][0]][start[1][1]]

    count += 1

path[f"{start[0][0]}{start[0][1]}"] = True
path[f"{start[1][0]}{start[1][1]}"] = True

total = 0
for i in range (len(map)):
    count = 0
    start = False
    for j in range (len(map[0])):
        key = f"{i}{j}"
        if key in path and not start:
            # print("hap", end=" ")
            start = True
            continue
        
        if not key in path and start:
            print(key, map[i][j], end= " ")
            # print("hep", end=" ")
            count += 1
            continue

        if key in path and start:
            # print("hop", end=" ")
            if not f"{i}{j-1}" in path :
                print(count, end= " ")
                start = False
                total += count
                count = 0
            continue

        if not key in path and not start:
            # print("hip", end=" ")
            continue

    print()
    # print(count)

print(total)
# print(path)

#the idea is storing the config
file = open("input.txt", "r")

map = []
for line in file.readlines():
    map.append(line.strip())

memPath = {}
memVisited = {}

prevVisit = [0, -1]
currVisit = [0, 0]

def followMap():
    queue = []
    queue.append([currVisit, prevVisit])

    while len(queue) > 0:
        currVisit, prevVisit = queue.pop(0)
        if f"{prevVisit[0]} {prevVisit[1]} {currVisit[0]} {currVisit[1]}" in memPath:
            continue

        if currVisit[0] >= len(map) or currVisit[0] < 0 or currVisit[1] >= len(map[0]) or currVisit[1] < 0:
            continue

        memPath[f"{prevVisit[0]} {prevVisit[1]} {currVisit[0]} {currVisit[1]}"] = True
        memVisited[f"{currVisit[0]} {currVisit[1]}"] = True

        temp0 = currVisit[0]
        temp1 = currVisit[1]
        curr0 = currVisit[0]
        curr1 = currVisit[1]

        if map[currVisit[0]][currVisit[1]] == ".":
            curr0 += currVisit[0] - prevVisit[0]
            curr1 += currVisit[1] - prevVisit[1]

            queue.append([[curr0, curr1], [temp0, temp1]])
        
        if map[currVisit[0]][currVisit[1]] == "\\":
            diffX = currVisit[0]-prevVisit[0]
            diffY = currVisit[1]-prevVisit[1]
            if diffY != 0:
                curr0 += diffY
            if diffX != 0:
                curr1 += diffX

            queue.append([[curr0, curr1], [temp0, temp1]])
        
        if map[currVisit[0]][currVisit[1]] == "/":
            diffX = currVisit[0]-prevVisit[0]
            diffY = currVisit[1]-prevVisit[1]
            if diffY != 0:
                curr0 -= diffY
            if diffX != 0:
                curr1 -= diffX
            
            queue.append([[curr0, curr1], [temp0, temp1]])

        if map[currVisit[0]][currVisit[1]] == "|":
            diffX = currVisit[0]-prevVisit[0]
            diffY = currVisit[1]-prevVisit[1]
            if diffX != 0:
                curr0 += diffX
                queue.append([[curr0, curr1], [temp0, temp1]])
            if diffY != 0:
                currNew0 = curr0 - 1
                curr0 += 1
                
                queue.append([[curr0, curr1], [temp0, temp1]])
                queue.append([[currNew0, curr1], [temp0, temp1]])

        if map[currVisit[0]][currVisit[1]] == "-":
            diffX = currVisit[0]-prevVisit[0]
            diffY = currVisit[1]-prevVisit[1]
            if diffX != 0:
                currNew1 = curr1 - 1
                curr1 += 1
                
                queue.append([[curr0, curr1], [temp0, temp1]])
                queue.append([[curr0, currNew1], [temp0, temp1]])
            if diffY != 0:
                curr1 += diffY
                queue.append([[curr0, curr1], [temp0, temp1]])

    print(len(memVisited.keys()))
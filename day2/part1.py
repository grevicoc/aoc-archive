'''
Idea:
Iterate each line and for one line, iterate each sets. For each set check is the number of cubes in accordance with the required numbers. If not skip it, if yes add it.

Complexity: O(n)
'''

mapReq = {
    "blue": 14,
    "green":13,
    "red" : 12
}

file = open("input.txt", "r")

total = 0
for line in file.readlines():
    split1 = line.split(":")
    id = int(split1[0].split(" ")[1])

    isBreak = False
    split2 = split1[1].split(";")
    for set in split2:
        split3 = set.split(",")
        for cubes in split3:
            cubesStripped = cubes.strip()
            split4 = cubesStripped.split(" ")
            if (int(split4[0]) > mapReq[split4[1]]):
                isBreak = True
                break
        
        if isBreak:
            break
    
    if isBreak:
        continue                                                                                                                                          
    
    # print(id)
    total += id
print(total)


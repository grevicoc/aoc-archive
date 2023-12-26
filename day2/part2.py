'''
Idea:
Iterate each line and for one line, iterate each sets. For each set store the maximum number of specific cube.

Complexity: O(n)
'''

file = open("input.txt", "r")

total = 0
for line in file.readlines():
    bareMin = {
        "blue": 0,
        "green": 0,
        "red": 0
    }
    split1 = line.split(":")
    id = int(split1[0].split(" ")[1])

    isBreak = False
    split2 = split1[1].split(";")
    for set in split2:
        split3 = set.split(",")
        for cubes in split3:
            cubesStripped = cubes.strip()
            split4 = cubesStripped.split(" ")
            if int(split4[0]) > bareMin[split4[1]]:
                bareMin[split4[1]] = int(split4[0])
                                                                                                                                       
    temp = 1
    for key in bareMin:
        if key != 0:
            temp = temp * bareMin[key]
    
    total += temp
print(total)


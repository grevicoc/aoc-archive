mapReq = {
    "blue": 14,
    "green":13,
    "red" : 12
}

file = open("input.txt", "r")

total = 0
for line in file.readlines():
    bareMin = {
        "blue": 0,
        "green": 0,
        "red": 0
    }
    split1 = line.split(":")
    # print(split1)
    id = int(split1[0].split(" ")[1])

    isBreak = False
    split2 = split1[1].split(";")
    # print(split2)
    for el in split2:
        split3 = el.split(",")
        # print(split3)
        for innerEl in split3:
            cleanInnerEl = innerEl.strip()
            # print(cleanInnerEl)
            split4 = cleanInnerEl.split(" ")
            if int(split4[0]) > bareMin[split4[1]]:
                bareMin[split4[1]] = int(split4[0])
            # if (int(split4[0]) > mapReq[split4[1]]):
            #     isBreak = True
            #     break
        
        # if isBreak:
        #     break
    
    # if isBreak:
    #     continue                                                                                                                                          
    temp = 1
    for key in bareMin:
        if key != 0:
            temp = temp * bareMin[key]
    
    # print(id)
    total += temp
print(total)


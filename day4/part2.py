'''
Idea:
Do the checking process like part 1 but we modified the calculation process. Now, we need to store card creation because for each winning number we need to create a copy of card after current card.

Complexity: O(nma) (n for set of winning number creation, m for number checking, and a for iteration of updating store card).
'''

file = open("input.txt", "r")

mapCard = {}
sum = 0
idx = 1
for line in file.readlines():
    if idx in mapCard:
        mapCard[idx] += 1
    else:
        mapCard[idx] = 1

    input = line.split(":")[1].strip("\n")
    separated = input.split("|")
    winning = separated[0]
    mine = separated[1]

    winNums = []
    for item in winning.split(" "):
        if item == "":
            continue
        num = int(item)
        winNums.append(num)

    count = 0
    for item in mine.split(" "):
        if item == "":
            continue
        num = int(item)
        if num in winNums:
            count += 1

    if count == 0:
        sum += mapCard[idx]
        idx += 1
        continue

    for i in range (idx+1, idx+count+1, 1):
        if i in mapCard:
            mapCard[i] += mapCard[idx]
        else:
            mapCard[i] = mapCard[idx]
    
    sum += mapCard[idx]
    idx += 1

print(mapCard)
print(sum)    
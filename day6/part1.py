file = open("input.txt", "r")

pairs = []
numString = file.readline().strip().split(":")[1].split(" ")
for num in numString:
    if num == "" or num == "\t":
        continue
    pairs.append([int(num)])

idx = 0
numString = file.readline().strip().split(":")[1].split(" ")
for num in numString:
    if num == "" or num == "\t":
        continue
    pairs[idx].append(int(num))
    idx += 1

total = 1
for pair in pairs:
    count = 0
    for speed in range (pair[0]+1):
        if speed * (pair[0]-speed) > pair[1]:
            count += 1
    print(count)
    total = total * count

print(pairs)
print(total)
    
    
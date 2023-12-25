file = open("input.txt", "r")

def calc(arr):
    allZero = True
    for num in arr:
        if num != 0:
            allZero = False
            break
    
    if allZero:
        return 0
    else:
        newList = []
        for i in range(len(arr)-1):
            newList.append(arr[i+1] - arr[i])
        
        return arr[0] - calc(newList)

sum = 0
for line in file:
    vals = line.strip().split(" ")
    intVals = []
    for val in vals:
        intVals.append(int(val))

    sum += calc(intVals)

print(sum)

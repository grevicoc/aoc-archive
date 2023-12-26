'''
Idea:
Iterate the array from the front and back. Store the value from the firstly-found on the front iteration and the firstly-found on the back iteration. Combine them for each line and at the end print the sum of all of it.

Complexity: O(2n) == O(n)
'''

file = open("input.txt", "r")
total = 0
for line in file.readlines():
    tempString = ""
    tempNum = ""
    for char in line:
        if (ord(char) >= 48 and ord(char) <=57):
            tempNum += char
            break

    tempString = ""
    for i in range (len(line)-1, -1, -1):
        if (ord(line[i]) >= 48 and ord(line[i]) <=57):
            tempNum += line[i]
            break

    # print(tempNum)
    num = int(tempNum)
    total += num

print(total)    
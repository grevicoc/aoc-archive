file = open("input.txt", "r")

num1 = ""
numString = file.readline().strip().split(":")[1].split(" ")
for num in numString:
    if num == "" or num == "\t":
        continue
    num1 += num
num1 = int(num1)
print(num1)

num2 = ""
numString = file.readline().strip().split(":")[1].split(" ")
for num in numString:
    if num == "" or num == "\t":
        continue
    num2 += num
num2 = int(num2)
print(num2)

count = 0
for speed in range (num1 + 1):
    if speed * (num1-speed) > num2:
        count += 1
print(count)
# total = total * count
    

# print(pairs)
# print(total)
    
    
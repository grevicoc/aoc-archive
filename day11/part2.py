file = open("input.txt", "r")

rowTwices = [True for i in range(len(file.readline().strip()))]
colTwices = [True for i in range(len(file.readline().strip()))]
file.seek(0)

i = 0
galaxies = []
for line in file.readlines():
    for j in range (len(line.strip())):
        if line[j] == "#":
            galaxies.append([i, j])
            rowTwices[i] = False
            colTwices[j] = False                                                                                     
    
    i += 1

# time = 0
sum = 0
for i in range (len(galaxies)):
    restGalaxies = galaxies[i+1:]
    for galaxy in restGalaxies:
        # time +=1
        count = 0
        additional = 0
        for row in range (galaxies[i][0], galaxy[0], 1):
            if rowTwices[row]:
                additional += 999999
            count += 1
        
        print(F"row {count}")
        yStart = galaxies[i][1]
        yEnd = galaxy[1]
        if yStart > yEnd:
            for col in range (yStart, yEnd, -1):
                if colTwices[col]:
                    additional += 999999
                count += 1
        else:
            for col in range (yStart, yEnd, 1):
                if colTwices[col]:
                    additional += 999999
                count += 1
        
        print(galaxies[i], galaxy)
        print(count, additional)
        print()
        sum += count + additional

print(sum)
# print(time)



# print(galaxies)
# print(rowTwices)
    
# 6, 1
# 11, 5
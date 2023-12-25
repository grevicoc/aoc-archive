import time

file = open("input.txt", "r")

lenCol = len(file.readline().strip())
file.seek(0)
lenRow = len(file.readlines())

upperBound = [lenRow for i in range(lenCol)]
file.seek(0)

class RoundRock:
    staticNumRock = 0

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.id = f"round {RoundRock.staticNumRock}"
        self.moveCnt = 0

        RoundRock.staticNumRock += 1
    
    def __str__(self) -> str:
        return f"{self.id}"

roundRocks = {}

rocks = []
total = 0
currRow = 0
for line in file.readlines():
    tempRowRocks = []
    currCol = 0
    for char in line.strip():
        if char == "O":
            obj = RoundRock(currRow, currCol)
            roundRocks[obj.id] = obj
            tempRowRocks.append(obj.id)
        else:
            tempRowRocks.append(char)

        currCol += 1

    rocks.append(tempRowRocks)
    currRow +=1

def north(rocks, roundRocks, cntSpin):
    for key in roundRocks.keys():
        if roundRocks[key].moveCnt >= cntSpin:
            continue
        
        willMoveRock = []
        row = roundRocks[key].x
        col = roundRocks[key].y
        while row >= 0 and rocks[row][col] != "#":
            if rocks[row][col] != "." and roundRocks[rocks[row][col]].moveCnt >= cntSpin:
                break

            if rocks[row][col] != ".":
                willMoveRock.append(rocks[row][col])

            row -= 1

        for idRock in willMoveRock:
            rock = roundRocks[idRock]
            
            before = rocks[rock.x][rock.y]
            row += 1
            after = rocks[row][rock.y]

            if before != "." and roundRocks[before].moveCnt >= cntSpin:
                rocks[rock.x][rock.y] = before
            else:
                rocks[rock.x][rock.y] = "."

            if after == ".":
                rocks[row][rock.y] = rock.id
            else:
                rocks[row][rock.y] = before

            rock.moveCnt += 1
            rock.x = row

def west(rocks, roundRocks, cntSpin):
    for key in roundRocks.keys():
        # print(key)
        if roundRocks[key].moveCnt >= cntSpin:
            continue
        
        willMoveRock = []
        row = roundRocks[key].x
        col = roundRocks[key].y
        # print(row, col)
        while col >= 0 and rocks[row][col] != "#":
            if rocks[row][col] != "." and roundRocks[rocks[row][col]].moveCnt >= cntSpin:
                break

            if rocks[row][col] != ".":
                # print(rocks[row][col])
                willMoveRock.append(rocks[row][col])

            col -= 1

        # print(willMoveRock)
        for idRock in willMoveRock:
            # print(idRock)
            rock = roundRocks[idRock]
            before = rocks[rock.x][rock.y]
            col += 1
            after = rocks[rock.x][col]

            if before != "." and roundRocks[before].moveCnt >= cntSpin:
                rocks[rock.x][rock.y] = before
            else:
                rocks[rock.x][rock.y] = "."

            if after == ".":
                rocks[rock.x][col] = rock.id
            else:
                rocks[rock.x][col] = before

            rock.moveCnt += 1
            rock.y = col

def south(rocks, roundRocks, cntSpin):
    for key in roundRocks.keys():
        if roundRocks[key].moveCnt >= cntSpin:
            continue
        
        willMoveRock = []
        row = roundRocks[key].x
        col = roundRocks[key].y
        while row < len(rocks) and rocks[row][col] != "#":
            if rocks[row][col] != "." and roundRocks[rocks[row][col]].moveCnt >= cntSpin:
                break

            if rocks[row][col] != ".":
                willMoveRock.append(rocks[row][col])

            row += 1

        for idRock in willMoveRock:
            rock = roundRocks[idRock]
            
            before = rocks[rock.x][rock.y]
            row -= 1
            after = rocks[row][rock.y]

            if before != "." and roundRocks[before].moveCnt >= cntSpin:
                rocks[rock.x][rock.y] = before
            else:
                rocks[rock.x][rock.y] = "."

            if after == ".":
                rocks[row][rock.y] = rock.id
            else:
                rocks[row][rock.y] = before

            rock.moveCnt += 1
            rock.x = row

def east(rocks, roundRocks, cntSpin):
    for key in roundRocks.keys():
        # print(key)
        if roundRocks[key].moveCnt >= cntSpin:
            continue
        
        willMoveRock = []
        row = roundRocks[key].x
        col = roundRocks[key].y
        # print(row, col)
        while col < len(rocks[0]) and rocks[row][col] != "#":
            if rocks[row][col] != "." and roundRocks[rocks[row][col]].moveCnt >= cntSpin:
                break

            if rocks[row][col] != ".":
                # print(rocks[row][col])
                willMoveRock.append(rocks[row][col])

            col += 1

        # print(willMoveRock)
        for idRock in willMoveRock:
            # print(idRock)
            rock = roundRocks[idRock]
            before = rocks[rock.x][rock.y]
            col -= 1
            after = rocks[rock.x][col]

            if before != "." and roundRocks[before].moveCnt >= cntSpin:
                rocks[rock.x][rock.y] = before
            else:
                rocks[rock.x][rock.y] = "."

            if after == ".":
                rocks[rock.x][col] = rock.id
            else:
                rocks[rock.x][col] = before

            rock.moveCnt += 1
            rock.y = col

def isSame(pattern1, pattern2):
    for i in range (len(pattern1)):
        for j in range ((len(pattern1[0]))):
            if pattern1[i][j] != pattern2[i][j]:
                return False
            
    return True

patterns = []
at_what = 0
for i in range (1, 4*1000000000, 1):
    if i%4 == 1:
        north(rocks,roundRocks,i)
    if i%4 == 2:
        west(rocks,roundRocks,i)
    if i%4 == 3:
        south(rocks,roundRocks,i)
    if i%4 == 0:
        east(rocks, roundRocks, i)
        # for line in rocks:
        #     for char in line:
        #         if char != "." and char != "#":
        #             print("O ", end="")
        #             continue
        #         print(f"{char} ", end="")
        #     print()
    
        # print()
        # time.sleep(1)

        same = False
        idxPattern = 0
        for pattern in patterns:
            if isSame(pattern, rocks):
                print(idxPattern)
                print('aaa')
                same = True
                print(i)
                at_what = i/4
                print(at_what)

                print(1000000000-idxPattern)
                break
            idxPattern += 1

        if same:
            break
        
        copyRocks = [[] for i in range(len(rocks))]
        for j in range(len(copyRocks)):
            copyRocks[j] = rocks[j].copy()
        
        patterns.append(copyRocks)
# print(at_what)
# print()
print(len(patterns))
# # print(i)
# # print(rocks)
# total = 0
currRow = len(rocks)
for line in patterns[-3]:
    for char in line:
        if char != "." and char != "#":
            # print(currRow)
            total += currRow
    currRow -= 1
print(total)
# for line in rocks:
#     for char in line:
#         if char != "." and char != "#":
#             print("0", end="")
#             continue
#         print(char, end="")
#     print()


# print(rocks)

# create key-value pair with key is the index value is the symbol
# create key-value pair with key is unique char and the value is the index
# create function north, west, south, east
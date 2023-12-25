file = open("input.txt", "r")

seeds = []
maps = {}
currMap = ""

for line in file.readlines():
    splittedLine = line.split(":")
    # print(splittedLine)
    if splittedLine[0] == "" or splittedLine[0] == "\n":
        continue

    if splittedLine[0] == "seeds":
        for item in splittedLine[1].split(" "):
            if item == "":
                continue
            seeds.append(int(item))
    elif splittedLine[0] == "seed-to-soil map":
        currMap = "seed-to-soil map"
    elif splittedLine[0] == "soil-to-fertilizer map":
        currMap = "soil-to-fertilizer map"
    elif splittedLine[0] == "fertilizer-to-water map":
        currMap = "fertilizer-to-water map"
    elif splittedLine[0] == "water-to-light map":
        currMap = "water-to-light map"
    elif splittedLine[0] == "light-to-temperature map":
        currMap = "light-to-temperature map"
    elif splittedLine[0] == "temperature-to-humidity map":
        currMap = "temperature-to-humidity map"
    elif splittedLine[0] == "humidity-to-location map":
        currMap = "humidity-to-location map"
    else:
        # print(line)
        # print(isSeedToSoil)
        nums = line.strip().split(" ")
        dst, src, offset = int(nums[0]), int(nums[1]), int(nums[2])
        if currMap in maps:
            maps[currMap].append([dst, src, offset])
        else:
            maps[currMap] = [[dst, src, offset]]

locations = []
idxSeed = 0
lowest = 2**63 - 1
while idxSeed < len(seeds):
    start = seeds[idxSeed]
    end = start + seeds[idxSeed+1] - 1

    rangesInput = [[start, end]]
    rangesMaps = maps["seed-to-soil map"]
    newRangesInput = []
    for input in rangesInput:
        unMappedRange = input
        for map in rangesMaps:
            lowerBound = map[1]
            upperBound = map[1] + map[2] -1
            diff = map[0] - map[1]

            if unMappedRange[0] >= lowerBound and unMappedRange[0] <= upperBound:
                if upperBound >= unMappedRange[1]:
                    newRangesInput.append([unMappedRange[0] + diff, unMappedRange[1] + diff])
                    unMappedRange = []
                    break
                else:
                    newRangesInput.append([unMappedRange[0] + diff, upperBound + diff])
                    unMappedRange = [upperBound+1, unMappedRange[1]]
            elif unMappedRange[1] >= lowerBound and unMappedRange[1] <= upperBound:
                if lowerBound <= unMappedRange[0]:
                    newRangesInput.append([unMappedRange[0] + diff, unMappedRange[1] + diff])
                    unMappedRange = []
                    break
                else:
                    newRangesInput.append([lowerBound + diff, unMappedRange[1] + diff])
                    unMappedRange = [unMappedRange[0], lowerBound-1]
    
        if len(unMappedRange) != 0:
            newRangesInput.append(unMappedRange)
        
    rangesInput = newRangesInput
    rangesMaps = maps["soil-to-fertilizer map"]
    newRangesInput = []
    for input in rangesInput:
        unMappedRange = input
        for map in rangesMaps:
            lowerBound = map[1]
            upperBound = map[1] + map[2] -1
            diff = map[0] - map[1]

            if unMappedRange[0] >= lowerBound and unMappedRange[0] <= upperBound:
                if upperBound >= unMappedRange[1]:
                    newRangesInput.append([unMappedRange[0] + diff, unMappedRange[1] + diff])
                    unMappedRange = []
                    break
                else:
                    newRangesInput.append([unMappedRange[0] + diff, upperBound + diff])
                    unMappedRange = [upperBound+1, unMappedRange[1]]
            elif unMappedRange[1] >= lowerBound and unMappedRange[1] <= upperBound:
                if lowerBound <= unMappedRange[0]:
                    newRangesInput.append([unMappedRange[0] + diff, unMappedRange[1] + diff])
                    unMappedRange = []
                    break
                else:
                    newRangesInput.append([lowerBound + diff, unMappedRange[1] + diff])
                    unMappedRange = [unMappedRange[0], lowerBound-1]
    
        if len(unMappedRange) != 0:
            newRangesInput.append(unMappedRange)

    rangesInput = newRangesInput
    rangesMaps = maps["fertilizer-to-water map"]
    newRangesInput = []
    for input in rangesInput:
        unMappedRange = input
        for map in rangesMaps:
            lowerBound = map[1]
            upperBound = map[1] + map[2] -1
            diff = map[0] - map[1]

            if unMappedRange[0] >= lowerBound and unMappedRange[0] <= upperBound:
                if upperBound >= unMappedRange[1]:
                    newRangesInput.append([unMappedRange[0] + diff, unMappedRange[1] + diff])
                    unMappedRange = []
                    break
                else:
                    newRangesInput.append([unMappedRange[0] + diff, upperBound + diff])
                    unMappedRange = [upperBound+1, unMappedRange[1]]
            elif unMappedRange[1] >= lowerBound and unMappedRange[1] <= upperBound:
                if lowerBound <= unMappedRange[0]:
                    newRangesInput.append([unMappedRange[0] + diff, unMappedRange[1] + diff])
                    unMappedRange = []
                    break
                else:
                    newRangesInput.append([lowerBound + diff, unMappedRange[1] + diff])
                    unMappedRange = [unMappedRange[0], lowerBound-1]
    
        if len(unMappedRange) != 0:
            newRangesInput.append(unMappedRange)
        
    rangesInput = newRangesInput
    rangesMaps = maps["water-to-light map"]
    newRangesInput = []
    for input in rangesInput:
        unMappedRange = input
        for map in rangesMaps:
            lowerBound = map[1]
            upperBound = map[1] + map[2] -1
            diff = map[0] - map[1]

            if unMappedRange[0] >= lowerBound and unMappedRange[0] <= upperBound:
                if upperBound >= unMappedRange[1]:
                    newRangesInput.append([unMappedRange[0] + diff, unMappedRange[1] + diff])
                    unMappedRange = []
                    break
                else:
                    newRangesInput.append([unMappedRange[0] + diff, upperBound + diff])
                    unMappedRange = [upperBound+1, unMappedRange[1]]
            elif unMappedRange[1] >= lowerBound and unMappedRange[1] <= upperBound:
                if lowerBound <= unMappedRange[0]:
                    newRangesInput.append([unMappedRange[0] + diff, unMappedRange[1] + diff])
                    unMappedRange = []
                    break
                else:
                    newRangesInput.append([lowerBound + diff, unMappedRange[1] + diff])
                    unMappedRange = [unMappedRange[0], lowerBound-1]
    
        if len(unMappedRange) != 0:
            newRangesInput.append(unMappedRange)

    rangesInput = newRangesInput
    rangesMaps = maps["light-to-temperature map"]
    newRangesInput = []
    for input in rangesInput:
        unMappedRange = input
        for map in rangesMaps:
            lowerBound = map[1]
            upperBound = map[1] + map[2] -1
            diff = map[0] - map[1]

            if unMappedRange[0] >= lowerBound and unMappedRange[0] <= upperBound:
                # print("here")
                # print(unMappedRange[0], unMappedRange[1], lowerBound, upperBound)
                if upperBound >= unMappedRange[1]:
                    newRangesInput.append([unMappedRange[0] + diff, unMappedRange[1] + diff])
                    unMappedRange = []
                    break
                else:
                    newRangesInput.append([unMappedRange[0] + diff, upperBound + diff])
                    unMappedRange = [upperBound+1, unMappedRange[1]]
            elif unMappedRange[1] >= lowerBound and unMappedRange[1] <= upperBound:
                # print("here2")
                # print(unMappedRange[0], unMappedRange[1], lowerBound, upperBound)
                if lowerBound <= unMappedRange[0]:
                    newRangesInput.append([unMappedRange[0] + diff, unMappedRange[1] + diff])
                    unMappedRange = []
                    break
                else:
                    newRangesInput.append([lowerBound + diff, unMappedRange[1] + diff])
                    unMappedRange = [unMappedRange[0], lowerBound-1]
    
        if len(unMappedRange) != 0:
            newRangesInput.append(unMappedRange)

    rangesInput = newRangesInput
    rangesMaps = maps["temperature-to-humidity map"]
    newRangesInput = []
    for input in rangesInput:
        unMappedRange = input
        for map in rangesMaps:
            lowerBound = map[1]
            upperBound = map[1] + map[2] -1
            diff = map[0] - map[1]

            if unMappedRange[0] >= lowerBound and unMappedRange[0] <= upperBound:
                # print("here")
                # print(unMappedRange[0], unMappedRange[1], lowerBound, upperBound)
                if upperBound >= unMappedRange[1]:
                    newRangesInput.append([unMappedRange[0] + diff, unMappedRange[1] + diff])
                    unMappedRange = []
                    break
                else:
                    newRangesInput.append([unMappedRange[0] + diff, upperBound + diff])
                    unMappedRange = [upperBound+1, unMappedRange[1]]
            elif unMappedRange[1] >= lowerBound and unMappedRange[1] <= upperBound:
                # print("here2")
                # print(unMappedRange[0], unMappedRange[1], lowerBound, upperBound)
                if lowerBound <= unMappedRange[0]:
                    newRangesInput.append([unMappedRange[0] + diff, unMappedRange[1] + diff])
                    unMappedRange = []
                    break
                else:
                    newRangesInput.append([lowerBound + diff, unMappedRange[1] + diff])
                    unMappedRange = [unMappedRange[0], lowerBound-1]
    
        if len(unMappedRange) != 0:
            newRangesInput.append(unMappedRange)
    
    rangesInput = newRangesInput
    rangesMaps = maps["humidity-to-location map"]
    newRangesInput = []
    for input in rangesInput:
        unMappedRange = input
        for map in rangesMaps:
            lowerBound = map[1]
            upperBound = map[1] + map[2] -1
            diff = map[0] - map[1]

            if unMappedRange[0] >= lowerBound and unMappedRange[0] <= upperBound:
                # print("here")
                # print(unMappedRange[0], unMappedRange[1], lowerBound, upperBound)
                if upperBound >= unMappedRange[1]:
                    newRangesInput.append([unMappedRange[0] + diff, unMappedRange[1] + diff])
                    unMappedRange = []
                    break
                else:
                    newRangesInput.append([unMappedRange[0] + diff, upperBound + diff])
                    unMappedRange = [upperBound+1, unMappedRange[1]]
            elif unMappedRange[1] >= lowerBound and unMappedRange[1] <= upperBound:
                # print("here2")
                # print(unMappedRange[0], unMappedRange[1], lowerBound, upperBound)
                if lowerBound <= unMappedRange[0]:
                    newRangesInput.append([unMappedRange[0] + diff, unMappedRange[1] + diff])
                    unMappedRange = []
                    break
                else:
                    newRangesInput.append([lowerBound + diff, unMappedRange[1] + diff])
                    unMappedRange = [unMappedRange[0], lowerBound-1]
    
        if len(unMappedRange) != 0:
            newRangesInput.append(unMappedRange)


    for item in newRangesInput:
        if item[0] < lowest:
            lowest = item[0]
    
    idxSeed += 2

print(lowest)
# print(maps)
# # locations.sort()
# print(locations)

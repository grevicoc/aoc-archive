'''
Idea:
First we need to create a container to store the mapping (use map). We dont need to store the whole values of 1-100 in the map, instead just store the offsets. Next, after the map is created, we can use the map to find the end result. For each map, check is there any offset that match the number, if not then the next number is the same, if yes then the next number is the current number + (dst-src).

Complexity: O(nm) (n for the map creation and m for the result finding).
'''

file = open("test.txt", "r")

seeds = []
maps = {}
currMap = ""

for line in file.readlines():
    splittedLine = line.split(":")
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
        nums = line.strip().split(" ")
        dst, src, offset = int(nums[0]), int(nums[1]), int(nums[2])
        if currMap in maps:
            maps[currMap].append([dst, src, offset])
        else:
            maps[currMap] = [[dst, src, offset]]

locations = []
for seed in seeds:
    next = seed
    ranges = maps["seed-to-soil map"]
    for item in ranges:
        if next >= item[1] and next <= item[1] + item[2] - 1:
            next = item[0] + (next - item[1])
            break
    
    ranges = maps["soil-to-fertilizer map"]
    for item in ranges:
        if next >= item[1] and next <= item[1] + item[2] - 1:
            next = item[0] + (next - item[1])
            break
    
    ranges = maps["fertilizer-to-water map"]
    for item in ranges:
        if next >= item[1] and next <= item[1] + item[2] - 1:
            next = item[0] + (next - item[1])
            break
    
    ranges = maps["water-to-light map"]
    for item in ranges:
        if next >= item[1] and next <= item[1] + item[2] - 1:
            next = item[0] + (next - item[1])
            break
    
    ranges = maps["light-to-temperature map"]
    for item in ranges:
        if next >= item[1] and next <= item[1] + item[2] - 1:
            next = item[0] + (next - item[1])
            break
    
    ranges = maps["temperature-to-humidity map"]
    for item in ranges:
        if next >= item[1] and next <= item[1] + item[2] - 1:
            next = item[0] + (next - item[1])
            break
    
    ranges = maps["humidity-to-location map"]
    for item in ranges:
        if next >= item[1] and next <= item[1] + item[2] - 1:
            next = item[0] + (next - item[1])
            break
    
    
    locations.append(next)

locations.sort()
print(locations)

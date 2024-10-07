import input

# Part 2

seeds = list(map(int, input.seeds.split()))

seeds = [seeds[i:i+2] for i in range(0, len(seeds), 2)]

maps = [input.seedToSoil, input.soilToFertilizer, input.fertilizerToWater, input.waterToLight, input.lightToTemperature, input.temperatureToHumidity, input.humidityToLocation]

for i in range(len(maps)):
    curr = []
    for line in maps[i].split("\n"):
        curr.append(list(map(int, line.split())))
    maps[i] = curr

notFound = seeds
for m in maps:
    print(notFound)
    found = []
    for dest, source, r in m:
        stillNotFound = []
        for start, numSeeds in notFound:
        # soilToFertilizer = """0 15 37
        #                       37 52 2
        #                       39 0 15"""
            end = start+numSeeds-1
            if start < source:
                if end < source:
                    stillNotFound.append([start, numSeeds])
                else:
                    stillNotFound.append([start, source-start])
                    if end >= source+r:
                        stillNotFound.append([source+r, end-(source+r)+1])
                        found.append([dest, r])
                    else:
                        found.append([dest, end-source+1])
            else:
                if start >= source+r:
                    stillNotFound.append([start, numSeeds])
                else:
                    if end < source+r:
                        found.append([dest+start-source, numSeeds])
                    else:
                        found.append([dest+start-source, source+r-start])
                        stillNotFound.append([source+r, end-(source+r)+1])
        notFound = stillNotFound
    notFound = notFound + found
print(notFound)
lowest = float("inf")
for s, _ in notFound:
    lowest = min(s, lowest)

print(lowest)


# Part 1

seeds = list(map(int, seeds.split()))
maps = [seedToSoil, soilToFertilizer, fertilizerToWater, waterToLight, lightToTemperature, temperatureToHumidity, humidityToLocation]

for i in range(len(maps)):
    curr = []
    for line in maps[i].split("\n"):
        curr.append(list(map(int, line.split())))
    maps[i] = curr

print(maps)
lowest = float("inf")
for seed in seeds:
    curr = seed
    found = False
    for map in maps:
        for dest, source, r in map:
            if curr >= source and curr < source + r:
                curr = dest + curr - source
                found = True
                break
    print("location", curr)
    lowest = min(curr, lowest)

print(lowest)
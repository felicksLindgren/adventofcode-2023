# Day 6

# Part 1

race = open("input.txt", "r").read().split("\n")
# Time:      7  15   30
# Distance:  9  40  200

def part_1():
    times = race[0].split(":")[1].strip().split()
    distances = race[1].split(":")[1].strip().split()
    map = {}

    for i in range(len(times)):
        time = int(times[i])
        benchmark_distance = int(distances[i])

        for speed in range(1, time + 1):
            distance = speed * (time - speed)

            if distance > benchmark_distance:
                if i in map:
                    map[i] += 1
                else:
                    map[i] = 1
            

    # Calculate the product of the values in the map
    product = 1
    for key in map:
        product *= map[key]

    print(product)

part_1()

# Part 2

race = open("input.txt", "r").read().split("\n")
# Time:      7  15   30
# Distance:  9  40  200

def part_2():
    # time = 71530
    # distance = 940200

    time = ''.join(race[0].split(":")[1].strip().split())
    distance_benchmark = ''.join(race[1].split(":")[1].strip().split())
    strategies = 0

    for speed in range(1, int(time) + 1):
        distance = speed * (int(time) - speed)

        if distance > int(distance_benchmark):
            strategies += 1
        
    print(strategies)

part_2()
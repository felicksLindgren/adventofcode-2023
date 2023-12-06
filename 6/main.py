# Day 6

# Part 1

race = open("input.txt", "r").read().split("\n")
# Time:      7  15   30
# Distance:  9  40  200


def part_1():
    times = race[0].split(":")[1].strip().split()
    distances = race[1].split(":")[1].strip().split()

    for i in range(len(times)):
        time = int(times[i])
        distance = int(distances[i])

        for j in range(time):
            if j == 0:
                continue

            # Milliseconds
            hold_start_button = j

            # Millimeters per millisecond 
            speed = j

            # Millimeters
            distance_covered = 0

            # Need to calculate how far we can travel in the time given

part_1()
# Day 5

# Part 1

# Read in the data
# almanac = open("input.txt", "r").read().split("\n")

def part_1():
    seeds = almanac[0].split(":")[1].strip().split(" ")
    current_map = ""
    map = {}

    # Skip first row in almanac
    for row in almanac[1:]:
        # Skip empty rows
        if row == "":
            continue

        # If the row contains a colon, it is a map  
        if ":" in row:
            current_map = row.split(":")[0].strip()
            continue

        # If the row starts with a number, it is a map entry
        if row[0].isdigit():
            values = row.split(" ")
            dest_range_start = int(values[0])
            source_range_start = int(values[1])
            range_length = int(values[2])

            for seed in seeds:
                seed = int(seed)
                if seed not in map:
                    map[seed] = {}

                # Check for a updated seed value in the map
                seed_value = seed
                if map[seed] != {}:
                    if current_map in map[seed]["map"]:
                        continue
                    else:
                        seed_value = map[seed]["seed"]

                if seed_value >= source_range_start and seed_value <= source_range_start + range_length:
                    map[seed] = {
                        "seed": dest_range_start + (seed_value - source_range_start),
                        "map": current_map
                    }

    # Calculate the key in map with the lowest seed value
    lowest_seed = -1
    for key in map:
        if lowest_seed == -1:
            lowest_seed = map[key]["seed"]
        if map[key]["seed"] < lowest_seed:
            lowest_seed = map[key]["seed"]

    print(lowest_seed)

# part_1()

# Part 2

# Read in the data
almanac = open("input.txt", "r").read().split("\n")

def part_2():
    seed_ranges = almanac[0].split(":")[1].strip().split(" ")

    odd_seeds = seed_ranges[0::2]
    even_seeds = seed_ranges[1::2]
    pair_seeds = zip(odd_seeds, even_seeds)

    for start, end in pair_seeds:
        start = int(start)
        end = int(end) + start
        seeds = range(start, end)

        current_map = ""
        map = {}

        # Skip first row in almanac
        for row in almanac[1:]:
            # Skip empty rows
            if row == "":
                continue

            # If the row contains a colon, it is a map  
            if ":" in row:
                current_map = row.split(":")[0].strip()
                continue

            # If the row starts with a number, it is a map entry
            if row[0].isdigit():
                values = row.split(" ")
                dest_range_start = int(values[0])
                source_range_start = int(values[1])
                range_length = int(values[2])

                for seed in seeds:
                    seed = int(seed)
                    if seed not in map:
                        map[seed] = {}

                    # Check for a updated seed value in the map
                    seed_value = seed
                    if map[seed] != {}:
                        if current_map in map[seed]["map"]:
                            continue
                        else:
                            seed_value = map[seed]["seed"]

                    if seed_value >= source_range_start and seed_value <= source_range_start + range_length:
                        map[seed] = {
                            "seed": dest_range_start + (seed_value - source_range_start),
                            "map": current_map
                        }

    # Calculate the key in map with the lowest seed value
    lowest_seed = -1
    for key in map:
        if lowest_seed == -1:
            lowest_seed = map[key]["seed"]
        if map[key]["seed"] < lowest_seed:
            lowest_seed = map[key]["seed"]

    print(lowest_seed)

part_2()
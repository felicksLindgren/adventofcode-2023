# Day 2: Cube Conundrum

# Part 1

record_of_games = open("input.txt", "r")

def part_1():
    sum_of_ids = 0

    for line in record_of_games:
        line = line.strip()
        games_is_possible = True
        title, game = line.split(":")
        id = title.split(" ")[1]
        sets = game.strip().split(";")

        for set in sets:
            bag_of_cubes = {
                "red": 12,
                "green": 13,
                "blue": 14,
            }
            cubes = set.strip().split(",")

            for cube in cubes:
                number, color = cube.strip().split(" ")

                bag_of_cubes[color] -= int(number)
                
                if bag_of_cubes[color] < 0:
                    games_is_possible = False
        
        if games_is_possible:
            sum_of_ids += int(id)

    print(sum_of_ids)

part_1()

# Part 2

record_of_games = open("input.txt", "r")

def part_2():
    sum_of_power_of_sets = 0

    for line in record_of_games:
        line = line.strip()
        title, game = line.split(":")
        id = title.split(" ")[1]
        sets = game.strip().split(";")

        bag_of_cubes = {
            "red": 0,
            "green": 0,
            "blue": 0,
        }

        for set in sets:
            cubes = set.strip().split(",")

            for cube in cubes:
                number, color = cube.strip().split(" ")
                number = int(number)

                if number > bag_of_cubes[color]:
                    bag_of_cubes[color] = number

        power_of_sets = bag_of_cubes["red"] * bag_of_cubes["green"] * bag_of_cubes["blue"]
        sum_of_power_of_sets += power_of_sets

    print(sum_of_power_of_sets)

part_2()
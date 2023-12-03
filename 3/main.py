# Day 3

# Part 1

print("Part 1")
engine_schematic = open("input.txt", "r").read().split("\n")

def sum_of_part_numbers():
    sum = 0
    symbols = ["*", "+", "$", "#", "/", "@", "-", "=", "%", "&"]
    part_number = ""
    is_part_number = False

    for x, row in enumerate(engine_schematic):
        for y, char in enumerate(row):
            if not char.isdigit():
                if is_part_number:
                    sum += int(part_number)
                is_part_number = False
                part_number = ""
                continue

            part_number += char
            east, south_east, south, south_west, west, north_west, north, north_east = 0, 0, 0, 0, 0, 0, 0, 0

            if x > 0:
                if y > 0:
                    north_west = engine_schematic[x - 1][y - 1]
                if y < len(row) - 1:
                    north_east = engine_schematic[x - 1][y + 1]
                north = engine_schematic[x - 1][y]

            if x < len(engine_schematic) - 2:
                if y > 0:
                    south_west = engine_schematic[x + 1][y - 1]
                if y < len(row) - 1:
                    south_east = engine_schematic[x + 1][y + 1]
                south = engine_schematic[x + 1][y]

            if y > 0:
                west = engine_schematic[x][y - 1]
            if y < len(row) - 1:
                east = engine_schematic[x][y + 1]

            if east in symbols or south_east in symbols or south in symbols or south_west in symbols or west in symbols or north_west in symbols or north in symbols or north_east in symbols:
                is_part_number = True
            
            
    print(sum)
            
sum_of_part_numbers()

# Part 2

print("Part 2")
engine_schematic = open("input.txt", "r").read().split("\n")

def sum_of_gear_ratios():
    sum = 0
    gear = "*"

    for x, row in enumerate(engine_schematic):
        for y, char in enumerate(row):
            if char is gear:
                # Check for gear ratio
                ratio_1 = 0
                ratio_2 = 0
                east, south_east, south, south_west, west, north_west, north, north_east = "0", "0", "0", "0", "0", "0", "0", "0"

                if x > 0:
                    if y > 0:
                        north_west = engine_schematic[x - 1][y - 1]
                    if y < len(row) - 1:
                        north_east = engine_schematic[x - 1][y + 1]
                    north = engine_schematic[x - 1][y]

                if x < len(engine_schematic) - 2:
                    if y > 0:
                        south_west = engine_schematic[x + 1][y - 1]
                    if y < len(row) - 1:
                        south_east = engine_schematic[x + 1][y + 1]
                    south = engine_schematic[x + 1][y]
                
                if y > 0:
                    west = engine_schematic[x][y - 1]
                if y < len(row) - 1:
                    east = engine_schematic[x][y + 1]

                if east.isdigit():
                    number = check_for_number(east, y + 1, engine_schematic[x])
                    if ratio_1 != 0 and ratio_1 != number:
                        ratio_2 = number
                    else:
                        ratio_1 = number

                if south_east.isdigit():
                    number = check_for_number(south_east, y + 1, engine_schematic[x + 1])
                    if ratio_1 != 0 and ratio_1 != number:
                        ratio_2 = number
                    else:
                        ratio_1 = number
                
                if south.isdigit():
                    number = check_for_number(south, y, engine_schematic[x + 1])
                    if ratio_1 != 0 and ratio_1 != number:
                        ratio_2 = number
                    else:
                        ratio_1 = number
                
                if south_west.isdigit():
                    number = check_for_number(south_west, y - 1, engine_schematic[x + 1])
                    if ratio_1 != 0 and ratio_1 != number:
                        ratio_2 = number
                    else:
                        ratio_1 = number

                if west.isdigit():
                    number = check_for_number(west, y - 1, engine_schematic[x])
                    if ratio_1 != 0 and ratio_1 != number:
                        ratio_2 = number
                    else:
                        ratio_1 = number

                if north_west.isdigit():
                    number = check_for_number(north_west, y - 1, engine_schematic[x - 1])
                    if ratio_1 != 0 and ratio_1 != number:
                        ratio_2 = number
                    else:
                        ratio_1 = number

                if north.isdigit():
                    number = check_for_number(north, y, engine_schematic[x - 1])
                    if ratio_1 != 0 and ratio_1 != number:
                        ratio_2 = number
                    else:
                        ratio_1 = number

                if north_east.isdigit():
                    number = check_for_number(north_east, y + 1, engine_schematic[x - 1])
                    if ratio_1 != 0 and ratio_1 != number:
                        ratio_2 = number
                    else:
                        ratio_1 = number

                if ratio_1 != 0 and ratio_2 != 0:
                    sum += int(ratio_1) * int(ratio_2)

    print(sum)

# Checks east and west for a number, a number can be max 3 digits long
def check_for_number(number, y, row):
    if row[y - 1].isdigit():
        number = f"{row[y - 1]}{number}"
        if row[y - 2].isdigit():
            number = f"{row[y - 2]}{number}"

    if row[y + 1].isdigit():
        number += row[y + 1]
        if row[y + 2].isdigit():
            number += row[y + 2]

    return number

                
sum_of_gear_ratios()
# Day 4

# Part 1

print("Part 1")
game_cards = open("input.txt", "r")


def sum_of_points():
    sum = 0

    for card in game_cards:
        points = 0
        name, numbers = card.split(":")
        winning_numbers = numbers.split("|")[0].strip().split()
        played_numbers = numbers.split("|")[1].strip().split()

        for number in played_numbers:
            if number in winning_numbers:
                if points == 0:
                    points += 1
                else:
                    points *= 2

        sum += points

    print(sum)

sum_of_points()

# Part 2

print("Part 2")

game_cards = open("input.txt", "r")

def count_scratchcards():
    instances_of_cards = {}

    for card in game_cards:
        points = 0
        name, numbers = card.split(":")
        id = int(name.split()[1])
        winning_numbers = numbers.split("|")[0].strip().split()
        played_numbers = numbers.split("|")[1].strip().split()

        if id in instances_of_cards:
            instances_of_cards[id] += 1
        else:
            instances_of_cards[id] = 1

        for number in played_numbers:
            if number in winning_numbers:
                points += 1

        for index, point in enumerate(range(points)):
            next_id = id + index + 1
            if next_id in instances_of_cards:
                instances_of_cards[next_id] += instances_of_cards[id]
            else:
                instances_of_cards[next_id] = instances_of_cards[id]

    print(sum(instances_of_cards.values()))

count_scratchcards()

        


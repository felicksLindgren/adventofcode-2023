# Day 4

# Part 1

print("Part 1")
game_cards = open("input.txt", "r")
# Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
# Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
# Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
# Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
# Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
# Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11


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

        
        for i in range(instances_of_cards[id]):
            for index, point in enumerate(range(points)):
                next_id = id + index + 1
                if next_id in instances_of_cards:
                    instances_of_cards[next_id] += 1
                else:
                    instances_of_cards[next_id] = 1

    print(sum(instances_of_cards.values()))

count_scratchcards()

        


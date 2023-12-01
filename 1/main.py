# Day 1: Trebuchet?!

# Read in input.txt
calculations = open("input.txt", "r")

# Part 1

def sum_of_calibrations():
    sum = 0

    for line in calculations:
        all_numbers = [int(s) for s in line if s.isdigit()]
        first_number = all_numbers[0]
        last_number = all_numbers[-1]

        sum += int(str(first_number) + str(last_number))

    print(sum)

# sum_of_calibrations()

# Part 2

valid_numbers = {
    "one": "one1one",
    "two": "two2two",
    "three": "three3three",
    "four": "four4four",
    "five": "five5five",
    "six": "six6six",
    "seven": "seven7seven",
    "eight": "eight8eight",
    "nine": "nine9nine",
}

def sum_of_calibrations():
    sum = 0

    for line in calculations:
        for word in valid_numbers:
            line = line.replace(word, valid_numbers[word])
        
        all_numbers = [int(s) for s in line if s.isdigit()]
        first_number = all_numbers[0]
        last_number = all_numbers[-1]

        sum += int(str(first_number) + str(last_number))

    print(sum)
        

sum_of_calibrations()
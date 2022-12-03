import string


def part1(input_data):
    duplicates = []
    for rucksack in input_data:
        length = int(len(rucksack) / 2)
        compartment1, compartment2 = rucksack[:length], rucksack[length:]
        duplicates.append(findduplicate(compartment1, compartment2))
    return sum(map(itemvalue, duplicates))


def findduplicate(l1, l2):
    for item in l1:
        if item in l2:
            return item


def findtriple(l1, l2, l3):
    for item in l1:
        if item in l2 and item in l3:
            return item


def itemvalue(item):
    lowercase_letters = list(string.ascii_lowercase)
    uppercase_letters = list(string.ascii_uppercase)
    if item in lowercase_letters:
        return lowercase_letters.index(item) + 1
    elif item in uppercase_letters:
        return uppercase_letters.index(item) + len(lowercase_letters) + 1


def part2(input_data):
    startindex = 0
    triples = []
    while startindex < len(input_data) - 2:
        group = input_data[startindex:startindex+3]
        triples.append(findtriple(*group))
        startindex += 3
    return sum(map(itemvalue, triples))


if __name__ == '__main__':
    with open('input.txt') as file:
        input_data = list(map(str.strip, file.readlines()))

    print('Part 1:', part1(input_data))
    print('Part 2:', part2(input_data))

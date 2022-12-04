import re


def part1(input_data):
    subset_pairs = []
    pattern = r'(\d+)-(\d+)'

    for pair in input_data:
        assignment1, assignment2 = pair.split(',')
        assignment1 = list(map(int, re.match(pattern, assignment1).groups()))
        assignment2 = list(map(int, re.match(pattern, assignment2).groups()))
        if (assignment1[0] >= assignment2[0] and assignment1[1] <= assignment2[1]) or (assignment2[0] >= assignment1[0] and assignment2[1] <= assignment1[1]):
            subset_pairs.append(pair)
    return len(subset_pairs)


def part2(input_data):
    subset_pairs = []
    pattern = r'(\d+)-(\d+)'

    for pair in input_data:
        assignment1, assignment2 = pair.split(',')
        assignment1 = list(map(int, re.match(pattern, assignment1).groups()))
        assignment2 = list(map(int, re.match(pattern, assignment2).groups()))
        if is_in_range(assignment1[0], assignment2) or is_in_range(assignment1[1], assignment2) or is_in_range(assignment2[0], assignment1) or is_in_range(assignment2[1], assignment1):
            # print('Overlapping pair:', pair)
            subset_pairs.append(pair)
    return len(subset_pairs)


def is_in_range(i, r):
    return i >= r[0] and i <= r[1]


if __name__ == '__main__':
    with open('input.txt') as file:
        input_data = list(map(str.strip, file.readlines()))

    print('Part 1:', part1(input_data))
    print('Part 2:', part2(input_data))
from collections import deque, defaultdict
from copy import deepcopy
import re

pattern = r'move (\d+) from (\d+) to (\d+)'


def part1(stacks, instructions):
    modified_stacks = deepcopy(stacks)
    for amount, source, dest in instructions:
        for _ in range(amount):
            modified_stacks[dest].appendleft(modified_stacks[source].popleft())
    result = ""
    for i in range(1, len(modified_stacks.keys()) + 1):
        result += modified_stacks[i].popleft()
    return result


def part2(stacks, instructions):
    modified_stacks = deepcopy(stacks)
    for amount, source, dest in instructions:
        stack_to_move = []
        for _ in range(amount):
            stack_to_move.append(modified_stacks[source].popleft())
        for box in stack_to_move[::-1]:
            modified_stacks[dest].appendleft(box)
    result = ""
    for i in range(1, len(modified_stacks.keys()) + 1):
        result += modified_stacks[i].popleft()
    return result


def print_stacks(stacks):
    print('----Stacks------')
    for i in range(1, len(stacks.keys()) + 1):
        print(' '.join(stacks[i]))
    print('\n')


if __name__ == '__main__':
    with open('input.txt') as file:
        input_data = file.readlines()

    stacks = defaultdict(deque)
    instructions = []
    box_length = 4

    for line in input_data:
        if line[0] != "m":
            curr_index = 0
            while curr_index < len(line):
                if line[curr_index] == "[":
                    stacks[int(curr_index / 4) + 1].append(line[curr_index+1])
                curr_index += box_length
        else:
            instructions.append(list(map(int, re.match(pattern, line).groups())))

    print('Part 1:', part1(stacks, instructions))
    print('Part 2:', part2(stacks, instructions))

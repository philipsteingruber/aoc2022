def part1(input_data):
    return max(elf_inventories)



def part2(input_data):
    sorted_inventories = sorted(input_data, reverse=True)
    return sum(sorted_inventories[:3])


if __name__ == '__main__':
    with open('input.txt') as file:
        input_data = file.readlines()

    elf_inventories = []
    running_sum = 0
    for line in input_data:
        if line != "\n":
            running_sum += int(line)
        else:
            elf_inventories.append(running_sum)
            running_sum = 0
    if (running_sum > 0):
        elf_inventories.append(running_sum)

    print('Part 1:', part1(elf_inventories))
    print('Part 2:', part2(elf_inventories))
def part1(input_data):
    beats = {"X": "C", "Y": "A", "Z": "B"}
    ties = {"X": "A", "Y": "B", "Z": "C"}

    score = 0
    for line in input_data:
        opponent_move, own_move = line.split()

        score += point_values[own_move]
        if ties[own_move] == opponent_move:
            score += 3
        elif beats[own_move] == opponent_move:
            score += 6
    return score


def part2(input_data):
    beats = {"A": "Z", "B": "X", "C": "Y"}
    ties = {"A": "X", "B": "Y", "C": "Z"}
    loses_to = {"A": "Y", "B": "Z", "C": "X"}


    score = 0
    for line in input_data:
        opponent_move, result = line.split()
        if result == "X":
            own_move = beats[opponent_move]
        elif result == "Y":
            own_move = ties[opponent_move]
            score += 3
        elif result == "Z":
            own_move = loses_to[opponent_move]
            score += 6
        score += point_values[own_move]
    return score


if __name__ == '__main__':
    with open('input.txt') as file:
        input_data = file.readlines()

    point_values = {"X": 1, "Y": 2, "Z": 3}


    print('Part 1:', part1(input_data))
    print('Part 2:', part2(input_data))
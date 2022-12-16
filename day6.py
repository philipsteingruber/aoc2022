def calc_marker(signal, marker_length):
    recent_characters = list(signal[0:marker_length])
    if len(set(recent_characters)) == len(recent_characters):
        return marker_length
    for index, char in enumerate(signal[marker_length:], marker_length):
        recent_characters.append(char)
        recent_characters = recent_characters[1:]
        if len(set(recent_characters)) == len(recent_characters):
            return index + 1


if __name__ == '__main__':
    with open('input.txt') as file:
        input_data = file.read().strip()

    print('Part 1:', calc_marker(input_data, 4))
    print('Part 2:', calc_marker(input_data, 14))

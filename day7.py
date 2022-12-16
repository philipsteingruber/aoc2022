from sys import maxsize

def build_dirs(input_data):
    dirs = []
    current_dir = None
    for line_no, line in enumerate(input_data, 1):
        if line.startswith('$'):
            command = line.split(' ')[1:]
            if command[0] == 'cd':
                if command[1] == '..':
                    current_dir = current_dir.parent
                else:
                    old_dir = current_dir
                    current_dir_name = command[1]
                    current_dir = Directory(dir_name=current_dir_name, parent=old_dir)
                    if old_dir is not None:
                        old_dir.dirs_contained.append(current_dir)
                    dirs.append(current_dir)
        else:
            if line.startswith('dir'):
                dir_name = line.split(' ')[1]
                current_dir.dirs_contained.append(Directory(dir_name=dir_name, parent=current_dir))
            else:
                file_size, file_name = line.split(' ')
                current_dir.files_contained.append(ContainedFile(file_name, int(file_size)))

    return dirs


def calc_dir_size(directory):
    total_size = sum([f.file_size for f in directory.files_contained])
    total_size += sum([calc_dir_size(d) for d in directory.dirs_contained])
    return total_size

def part1(dirs):
    result = 0
    for directory in dirs:
        dir_size = calc_dir_size(directory)
        if dir_size <= 100000:
            result += dir_size
    return result


def part2(dirs):
    unused_space = 70000000 - calc_dir_size(dirs[0])
    required_space = 30000000
    diff = required_space - unused_space

    dir_sizes = sorted(list(map(calc_dir_size, dirs)))
    for dir_size in dir_sizes:
        if dir_size > diff:
            return dir_size


class Directory:
    def __init__(self, dir_name, parent=None):
        self.dir_name = dir_name
        self.parent = parent
        self.dirs_contained = []
        self.files_contained = []


class ContainedFile:
    def __init__(self, file_name, file_size):
        self.file_name = file_name
        self.file_size = file_size


if __name__ == '__main__':
    with open('input.txt') as file:
        input_data = list(map(str.strip, file.readlines()))

    dirs = build_dirs(input_data)

    print('Part 1:', part1(dirs))
    print('Part 2:', part2(dirs))
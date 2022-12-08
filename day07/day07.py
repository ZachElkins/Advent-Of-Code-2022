from helpers.file_reader import FileReader
from pathlib import Path


def update_path(cmd, path):
    cmd = cmd.split()
    if cmd[1] == "..":
        return path[:-1]
    else:
        path.append(cmd[1])
        return path


def build_file_system(cmds):
    file_system = {"/": {}}
    path = ["/"]

    for cmd in cmds:
        if cmd == "$ ls": continue
        if cmd.startswith("$ cd"):
            path = update_path(cmd[2:], path)
        else:
            cwd = file_system
            for d in path: cwd = cwd[d]

            cmd = cmd.split()

            cwd[cmd[1]] = {} if cmd[0] == "dir" else (int(cmd[0]))
    
    return file_system


size = 0 
def directory_size(directory):
    global size
    current_size = 0

    for i in directory.values():
        current_size += directory_size(i) if isinstance(i, dict) else i

    if current_size <= 100000: size += current_size

    return current_size


def part_one(file_system):
    directory_size(file_system)
    print(f"The combined size of directories smaller than 100000 is {size}.")


def file_system_size(size, file_system):
    current_size = 0
    for d in file_system.values():
        if isinstance(d, int): current_size += d 
        else: current_size += file_system_size(size+current_size, d)

    size += current_size

    return current_size


min_to_free = 70000000
def find_min_to_free(to_free, file_system):
    global min_to_free
    current_size = 0
    for d in file_system.values():
        if isinstance(d, int): current_size += d
        else: current_size += find_min_to_free(to_free, d)


    if to_free <= current_size and current_size < min_to_free:
        min_to_free = current_size

    return current_size
    

def part_two(file_system):
    max_space = 70000000
    required_space = 30000000
    to_free = required_space - (max_space - file_system_size(0, file_system))
    
    find_min_to_free(to_free, file_system)

    print(f"The smallest directory we can delete to free up at least 30000000 has a size of {min_to_free}.")


def main():
    lines = FileReader.read_lines(Path(__file__).parent.absolute())

    file_system = build_file_system(lines[1:])

    part_one(file_system)
    part_two(file_system)


if __name__ == "__main__":
    main()
from helpers.file_reader import FileReader
from pathlib import Path

from string import ascii_uppercase as uppers
from string import ascii_lowercase as lowers

def part_one(lines, values):
    priority = 0
    for line in lines:
        h = len(line)//2
        l = set(line[0: h])
        r = set(line[h: len(line)])
        priority += values[l.intersection(r).pop()]

    print(f"The final priority sum is {priority}.")


def part_two(lines, values):
    priority = 0
    for i in range(0, len(lines), 3):
        l1, l2, l3 = set(lines[i]), set(lines[i+1]), set(lines[i+2])
        priority += values[
            l1.intersection(l2).intersection(l3).pop()
        ]
    
    print(f"The final priority sum is {priority}.")


def main():
    lines = FileReader.read_lines(Path(__file__).parent.absolute())
    values = {letter: i+1 for i, letter in enumerate(lowers)}
    up_values = {letter: i+27 for i, letter in enumerate(uppers)}
    values.update(up_values)

    part_one(lines, values)
    part_two(lines, values)


if __name__ == "__main__":
    main()
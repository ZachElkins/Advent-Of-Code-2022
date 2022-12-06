from helpers.file_reader import FileReader
from pathlib import Path

def contains_fully(a, b):
    return int(a[0]) <= int(b[0]) and int(a[1]) >= int(b[1])

def contains_partially(a, b):
    return any([
        int(a[0]) <= int(b[0]) and int(a[1]) >= int(b[0]), 
        int(a[1]) >= int(b[1]) and int(a[0]) <= int(b[1])
    ])

def part_one(lines):
    overlap = 0
    for line in lines:
        splt = line.split(",")
        first, second = splt[0], splt[1]
        first_splt, second_splt = first.split("-"), second.split("-")
        if contains_fully(first_splt, second_splt) or contains_fully(second_splt, first_splt):
            overlap += 1

    print(f"The assignments fully overlap {overlap} times.")


def part_two(lines):
    overlap = 0
    for line in lines:
        splt = line.split(",")
        first, second = splt[0], splt[1]
        first_splt, second_splt = first.split("-"), second.split("-")
        if contains_partially(first_splt, second_splt) or contains_partially(second_splt, first_splt):
            overlap += 1

    print(f"The assignments partially overlap {overlap} times.")



def main():
    lines = FileReader.read_lines(Path(__file__).parent.absolute())

    part_one(lines)
    part_two(lines)


if __name__ == "__main__":
    main()
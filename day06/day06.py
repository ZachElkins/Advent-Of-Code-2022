from helpers.file_reader import FileReader
from pathlib import Path


def find_marker(buffer, marker_len):
    for i in range(0, len(buffer)-marker_len):
        marker = [buffer[i+j] for j in range(0, marker_len)]
        if len(set(marker)) == marker_len:
            return i+marker_len


def part_one(buffer):
    print(f"The message starts are character {find_marker(buffer, 4)}. (4-char start-marker)")


def part_two(buffer):
    print(f"The message starts are character {find_marker(buffer, 14)}. (14-char start-marker)")


def main():
    buffer = FileReader.read_line(Path(__file__).parent.absolute())

    part_one(buffer)
    part_two(buffer)


if __name__ == "__main__":
    main()
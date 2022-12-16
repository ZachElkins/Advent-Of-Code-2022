from helpers.file_reader import FileReader
from pathlib import Path
import re


def part_two(lines):
    
    print(f"{lines}")


def main():
    lines = FileReader.read_lines(Path(__file__).parent.absolute())
    
    part_two(lines)


if __name__ == "__main__":
    main()
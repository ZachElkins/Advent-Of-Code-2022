from helpers.file_reader import FileReader
from pathlib import Path
import heapq


def part_one(lines):
    max_calories = 0
    calories = 0
    for line in lines:
        if line == "":
            if calories > max_calories:
                max_calories = calories
            calories = 0
            continue
        calories += int(line)
    
    print(f"The elf carrying the most calories has {max_calories} calories.")


def part_two(lines):
    max_calories = []
    calories = 0
    for line in lines:
        if line == "":
            if len(max_calories) < 3:
                heapq.heappush(max_calories, calories)
            if calories > min(max_calories):
                heapq.heapreplace(max_calories, calories)
            calories = 0
            continue
        calories += int(line)

    print(f"The three elves carrying the most calories were carring a total of {sum(max_calories)} - {max_calories}")


def main():
    lines = FileReader.read_lines(Path(__file__).parent.absolute())

    part_one(lines)
    part_two(lines)


if __name__ == "__main__":
    main()
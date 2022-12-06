from helpers.file_reader import FileReader
from pathlib import Path


def part_one(lines):
    wins = ["CX", "AY", "BZ"]
    ties = ["AX", "BY", "CZ"]
    values = {"X": 1, "Y": 2, "Z": 3}
    score = 0
    for line in lines:
        op, me = line.split()
        outcome = f"{op}{me}"
        if outcome in ties:
            pts = values[me]+3
        else:
            pts = values[me]
            pts += 6 if outcome in wins else 0
        score += pts
    
    print(f"Your final score is {score}.")


def part_two(lines):
    outcomes = {"C": ["A", "B"], "A": ["B", "C"], "B": ["C", "A"]}
    values = {"A": 1, "B": 2, "C": 3}
    score = 0
    for line in lines:
        op, me = line.split()
        if me == "X":
            pts = values[outcomes[op][1]]
        elif me == "Y":
            pts = values[op]+3
        else:
            pts = values[outcomes[op][0]]+6
        score += pts
    
    print(f"Your final score is {score}.")


def main():
    lines = FileReader.read_lines(Path(__file__).parent.absolute())
    
    part_one(lines)
    part_two(lines)


if __name__ == "__main__":
    main()
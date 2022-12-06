from helpers.file_reader import FileReader
from pathlib import Path
from dataclasses import dataclass
from copy import deepcopy


@dataclass
class Instruction:
    qt: int
    fr: int
    to: int


def part_one(stacks, instructions):

    for instruction in instructions:
        for _ in range(instruction.qt):
            to_move = stacks[instruction.fr].pop()
            stacks[instruction.to].append(to_move)

    out = ""
    keys = list(stacks.keys())
    keys.sort()
    for i in keys:
        out = out+stacks[i][-1]

    print(f"The boxes on the top of each stack are {out} (Using the CrateMover 9000)")


def part_two(stacks, instructions):
    
    for instruction in instructions:
        to_move = stacks[instruction.fr][-instruction.qt:]
        left_over = stacks[instruction.fr][:-instruction.qt]
        stacks[instruction.fr] = left_over
        stacks[instruction.to] = stacks[instruction.to] + to_move

    out = ""
    keys = list(stacks.keys())
    keys.sort()
    for i in keys:
        out = out+stacks[i][-1]
        
    print(f"The boxes on the top of each stack are {out} (Using the CrateMover 9001)")


def main():
    lines = FileReader.read_lines_raw(Path(__file__).parent.absolute())
    mh = 8
    
    stacks = {}

    for line in lines[:mh]:
        for i in range(1, len(line), 2):
            f = lambda x: round(x//4)+1
            if line[i] != " " and line[i] != "\n":
                if f(i) in stacks:
                    stacks[f(i)].insert(0, line[i])
                else:
                    stacks[f(i)] = [line[i]]

    instructions = []
    
    for line in lines[mh+2:]:
        inst = line.split()
        instructions.append(
            Instruction(qt=int(inst[1]), fr=int(inst[3]), to=int(inst[5]))
        )

    part_one(deepcopy(stacks), instructions)
    part_two(deepcopy(stacks), instructions)


if __name__ == "__main__":
    main()
from helpers.file_reader import FileReader
from pathlib import Path


def part_one(operations):
    coi = {20: -1, 60: -1, 100: -1, 140: -1, 180: -1, 220: -1}
    cycles_per_op = {"noop": 1, "addx": 2}
    ops = [[op, cycles_per_op[op.split()[0]]] for op in operations]
    
    x = 1
    cycles = 1
    while ops:

        if cycles in coi:
            coi[cycles] = cycles*x
            
        cycles += 1
        ops[0][1] -=1

        if ops[0][1] > 0:
            continue

        if ops[0][0].startswith("noop"):
            ops.pop(0)
            continue

        x += int(ops.pop(0)[0].split()[1])

    print(sum(list(coi.values())))


def part_two(operations):
    cycles_per_op = {"noop": 1, "addx": 2}
    ops = [[op, cycles_per_op[op.split()[0]]] for op in operations]
    
    values = [0]*242

    x = 1
    cycles = 1
    while ops:

        cycles += 1
        values[cycles] = x

        ops[0][1] -=1

        if ops[0][1] > 0:
            continue

        if ops[0][0].startswith("noop"):
            ops.pop(0)
            continue

        x += int(ops.pop(0)[0].split()[1])

    for i, pixel in enumerate(values[2:]):
        crt = i % 40
        if crt == 0: print()
        if crt in [pixel-1, pixel, pixel+1]:
            print("#", end="")
        else:
            print(".", end="")
    

def main():
    lines = FileReader.read_lines(Path(__file__).parent.absolute())

    part_one(lines)
    part_two(lines)


if __name__ == "__main__":
    main()
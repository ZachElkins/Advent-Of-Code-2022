from helpers.file_reader import FileReader
from pathlib import Path
from ast import literal_eval
from itertools import zip_longest
from functools import cmp_to_key
from copy import deepcopy

def compare_packets(p1, p2):
    for a, b in zip_longest(p1, p2):
        if a == None: return True
        elif b == None:  return False
        elif type(a) == int and type(b) == int:
            if a != b: return a < b
        elif type(a) == list and type(b) == list:
            c = compare_packets(a, b)
            if c != -1: return c
        
        else:
            c = compare_packets([a], b) if type(a) == int else compare_packets(a, [b])
            if c != -1: return c

    return -1


def bsort(packets):

    n = len(packets)

    for i in range(n):
        for j in range(0, n - i - 1):
            if not compare_packets(packets[j], packets[j + 1]):
                packets[j], packets[j + 1] = packets[j + 1], packets[j]

    return packets

def part_one(lines):
    packets = [(literal_eval(l[0]), literal_eval(l[1])) for l in lines]
    valid = []
    for i, packet in enumerate(packets):
        if compare_packets(packet[0], packet[1]):
            valid.append(i+1)

    print(f"The sum of the valid packets is {sum(valid)}.")


def part_two(lines):
    keys = [[[2]], [[6]]]
    packets = deepcopy(keys)
    for line in lines:
        packets.append(literal_eval(line[0]))
        packets.append(literal_eval(line[1]))
    
    key_positions = []
    for i, packet in enumerate(bsort(packets)):
        if packet in keys:
            key_positions.append(i+1)
            if len(key_positions) == 2: break

    print(f"The decoder key is {(key_positions[0]*key_positions[1])}.")

def main():
    lines = FileReader.read_groups(Path(__file__).parent.absolute())

    part_one(lines)
    part_two(lines)


if __name__ == "__main__":
    main()
from helpers.file_reader import FileReader
from pathlib import Path
import re


def manhattan_distance(ax, ay, bx, by):
    return abs(ax-bx)+abs(ay-by)


def extract_locations(lines):
    data = []
    for line in lines:
        v = re.findall("x=(-?\d*), y=(-?\d*)", line)
        data.append((int(v[0][0]), int(v[0][1]), int(v[1][0]), int(v[1][1])))
    
    return data


def get_min_and_max(data):
    for s, b in data.items():
        if s[0] > max_x: max_x = s[0]
        elif s[0] < min_x: min_x = s[0]
        if s[1] > max_y: max_y = s[1]
        elif s[1] < min_y: min_y = s[1]
        if b[0] > max_x: max_x = b[0]
        elif b[0] < min_x: min_x = b[0]
        if b[1] > max_y: max_y = b[1]
        elif b[1] < min_y: min_y = b[1]

    return min_x, min_y, max_x, max_y


def get_empty(target, dists):
    empty_ranges = []
    for s, d in dists.items():
        if s[1] > target:
            if s[1]-d > target: continue
            dt = s[1]-target
            w = d-dt
            empty_ranges.append((s[0]-w, s[0]+w))
        elif s[1] < target:
            if s[1]+d < target: continue
            dt = target-s[1]
            w = d-dt
            empty_ranges.append((s[0]-w, s[0]+w))
        elif s[1] == target:
            empty_ranges.append((s[0]-d+1, s[0]+d-1))

    return empty_ranges


def overlap(r1, r2):
    return r1[1] >= r2[0] - 1


def merge(a, b):
    return (min(a[0], b[0]), max(a[1], b[1]))


def regroup(ranges):
    if len(ranges) == 0:
        return ranges

    ranges.sort()

    regrouped = [ranges[0]]

    for r2 in ranges[1:]:
        r1 = regrouped.pop()
        if overlap(r1, r2):
            regrouped.append(merge(r1, r2))
        else:
            regrouped.append(r1)
            regrouped.append(r2)

    return regrouped


def part_one(lines, target):
    data = extract_locations(lines)
    dists = {}
    beacons = set()
    for sx, sy, bx, by in data:
        beacons.add((bx, by))
        dists[(sx, sy)] = manhattan_distance(sx, sy, bx, by)

    empty_ranges = get_empty(target, dists)
    empty_ranges = regroup(empty_ranges)
    
    total_empty = 0
    for r in empty_ranges:
        if r[0] < 0:
            total_empty += r[1]-r[0]+1
        else:
            total_empty += r[1]-r[0]+1
        for b in beacons:
            if b[1] == target and b[0] >= r[0] and b[0] <= r[1]:
                total_empty -= 1

    print(f"There are {total_empty} spots in row {target} that do not have a beacon.")


def part_two(lines, target_range):
    data = extract_locations(lines)
    dists = {}
    beacons = set()
    for sx, sy, bx, by in data:
        beacons.add((bx, by))
        dists[(sx, sy)] = manhattan_distance(sx, sy, bx, by)

    for target in range(target_range):
        empty_ranges = get_empty(target, dists)
        empty_ranges = regroup(empty_ranges)
        if len(empty_ranges) >= 2:
            print(f"The tuning frequency is ({target_range*(empty_ranges[0][1]+1)+target}). (There is no beacon at ({target}, {empty_ranges[0][1]+1})!)")
            break


def main():
    lines = FileReader.read_lines(Path(__file__).parent.absolute())
    
    target = 2000000
    part_one(lines, target)

    target_range = 4000000
    part_two(lines, target_range)


if __name__ == "__main__":
    main()
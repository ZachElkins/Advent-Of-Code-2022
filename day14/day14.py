from helpers.file_reader import FileReader
from pathlib import Path


def draw_cave(cave):
    for c in range(len(cave[0])):
        for r in range(len(cave)):
            print(cave[r][c], end="")
        print()


def place_rocks(cave, wind_lines):
    for points in wind_lines:
        cave[points[0][0]][points[0][1]] = "#"
        cave[points[1][0]][points[1][1]] = "#"
        if points[0][0] == points[1][0] and points[0][1] >= points[1][1]:
            for i in range(0, points[0][1]-points[1][1]):
                cave[points[1][0]][points[1][1]+i] = "#"
        elif points[0][0] == points[1][0] and points[0][1] <= points[1][1]:
            for i in range(0, points[1][1]-points[0][1]):
                cave[points[0][0]][points[0][1]+i] = "#"
        elif points[0][1] == points[1][1] and points[0][0] >= points[1][0]:
            for i in range(0, points[0][0]-points[1][0]):
                cave[points[1][0]+i][points[1][1]] = "#"
        elif points[0][1] == points[1][1] and points[0][0] <= points[1][0]:
            for i in range(0, points[1][0]-points[0][0]):
                cave[points[0][0]+i][points[0][1]] = "#"
    return cave


def get_wind_lines(lines):
    coord_group = []
    for line in lines:
        coord_group.append([(int(point.split(",")[0]), int(point.split(",")[1])) for point in line.split("->")])

    min_w = min([min([point[0] for point in points]) for points in coord_group])
    max_w = max([max([point[0] for point in points]) for points in coord_group])
    w = max_w - min_w+1
    h = max([max([point[1] for point in points]) for points in coord_group])
    cave = [["." for _ in range(h+1)] for _ in range(w)]

    wind_lines = []
    for coord in coord_group:
        for  i in range(len(coord)):
            if i == 0: continue
            point_a = [coord[i-1][0]-min_w, coord[i-1][1]]
            point_b = [coord[i][0]-min_w, coord[i][1]]
            wind_lines.append([point_a, point_b])

    return cave, wind_lines, min_w


def get_wind_lines_2(lines):
    coord_group = []
    for line in lines:
        coord_group.append([(int(point.split(",")[0]), int(point.split(",")[1])) for point in line.split("->")])

    h = max([max([point[1] for point in points]) for points in coord_group])+3
    min_w = 500 - h
    max_w = 500 + h
    w = max_w - min_w+1
    cave = [["." for _ in range(h)] for _ in range(w)]

    wind_lines = []
    for coord in coord_group:
        for  i in range(len(coord)):
            if i == 0: continue
            point_a = [coord[i-1][0]-min_w, coord[i-1][1]]
            point_b = [coord[i][0]-min_w, coord[i][1]]
            wind_lines.append([point_a, point_b])

    return cave, wind_lines, min_w

def drop_sand(cave, source):
    sand = 0
    new_sand = source.copy()
    cave[source[0]][source[1]] = "+"
    while sand < 10**3:
        if new_sand[1] >= len(cave[0])-1 or new_sand[0] < 0:
            break
        if cave[new_sand[0]][new_sand[1]+1] == ".":
            new_sand[1] += 1
        elif cave[new_sand[0]-1][new_sand[1]+1] == ".":
            new_sand[0] -= 1
            new_sand[1] += 1
        elif cave[new_sand[0]+1][new_sand[1]+1] == ".":
            new_sand[0] += 1
            new_sand[1] += 1
        else:
            cave[new_sand[0]][new_sand[1]] = "o"
            new_sand = source.copy()
            sand+=1

    return cave, sand


def drop_sand_infinite_floor(cave, source):
    sand = 0
    new_sand = source.copy()
    cave[source[0]][source[1]] = "+"
    while sand < 10**5:
        if cave[new_sand[0]][new_sand[1]+1] == ".":
            new_sand[1] += 1
        elif cave[new_sand[0]-1][new_sand[1]+1] == ".":
            new_sand[0] -= 1
            new_sand[1] += 1
        elif cave[new_sand[0]+1][new_sand[1]+1] == ".":
            new_sand[0] += 1
            new_sand[1] += 1
        elif new_sand == source:
            cave[new_sand[0]][new_sand[1]] = "o"
            sand+=1
            break
        else:
            cave[new_sand[0]][new_sand[1]] = "o"
            new_sand = source.copy()
            sand+=1

    return cave, sand


def part_one(lines):
    cave, wind_lines, min_w = get_wind_lines(lines)
    cave = place_rocks(cave, wind_lines)
    source = [500-min_w, 0]
    cave, sand = drop_sand(cave, source)

    # draw_cave(cave)
    print(f"The first grain of sand falls off the edge after {sand} grains come to rest.")


def part_two(lines):
    cave, wind_lines, min_w = get_wind_lines_2(lines)
    cave = place_rocks(cave, wind_lines)
    for i in range(len(cave)):
        cave[i][-1] = "#"
    source = [500-min_w, 0]
    cave, sand = drop_sand_infinite_floor(cave, source)

    # draw_cave(cave)
    print(f"The sand source is plugged after {sand} grains come to rest.")


def main():
    lines = FileReader.read_lines(Path(__file__).parent.absolute())

    part_one(lines)
    part_two(lines)


if __name__ == "__main__":
    main()
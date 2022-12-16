from helpers.file_reader import FileReader
from pathlib import Path
from math import dist


def diag(a, b):
    return a[0] != b[0] and a[1] != b[1]


def make_moves(visited, moves, h, t):
    adding = []
    last_h = h
    
    for i, move in enumerate(moves):
        h = move
        print(f"> mv h {h}", end=" ")
        if i > 0 and dist(h, t) > 1.45:
            t = last_h
            visited.add(t)
            adding.append(t)
            print(f"> mv t {last_h}", end=" ")
        # elif dist(h, t) <= 1:
        #     print(f"> {h}, {t} {dist(h,t)}", end=" ")
        last_h = h
        print("")
    print("Adding ", adding)

    return visited, h, t

def part_one(lines):
    visited = set({(0,0)})
    h, t = (0, 0), (0, 0)

    for line in lines:
        d, q = line.split()
        print(f"========== {line} ==========")
        # print(f"{line} |",end=" ")
        if d == "L":
            visited, h, t, = make_moves(visited, [(h[0]-x, h[1]) for x in range(1, int(q)+1)], h, t)
        elif d == "R":
            visited, h, t, = make_moves(visited, [(h[0]+x, h[1]) for x in range(1, int(q)+1)], h, t)
        elif d == "U":
            visited, h, t, = make_moves(visited, [(h[0], h[1]+y) for y in range(1, int(q)+1)], h, t)
        else:
            visited, h, t, = make_moves(visited, [(h[0], h[1]-y) for y in range(1, int(q)+1)], h, t)

    print(visited)
    print(f"{len(visited)}")
 

def part_two(lines):
    out = ""

    print(f"{out}")
    

def main():
    lines = FileReader.read_lines(Path(__file__).parent.absolute())
    # lines = [
    #     "R 4",
    #     "U 4",
    #     "L 3",
    #     "D 1",
    #     "R 4",
    #     "D 1",
    #     "L 5",
    #     "R 2"
    # ]
    part_one(lines)
    part_two(lines)


if __name__ == "__main__":
    main()
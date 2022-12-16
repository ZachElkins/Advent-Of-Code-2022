from helpers.file_reader import FileReader
from pathlib import Path
from dataclasses import dataclass
from string import ascii_lowercase as lowers


@dataclass
class Point:
    x: int
    y: int
    val: int
    def pos(self):
        return (self.x, self.y)


def get_height_map(lines):
    vals = {letter: i for i, letter in enumerate(lowers)}

    g = []
    s, e = None, None
    r, c = 0, 0
    for line in lines:
        g.append([])
        for letter in line:
            if letter == "S":
                s = Point(c, r, -1)
                g[-1].append(Point(c, r, -1))
            elif letter == "E":
                e = Point(c, r, 26)
                g[-1].append(Point(c, r, 26))
            else:
                g[-1].append(Point(c, r, vals[letter]))
            c += 1
        c = 0
        r += 1
    return s, e, g


def neighbors(p, g):
    n = []
    x, y = p.pos()
    # Up
    if y < len(g)-1 and any([
        g[y+1][x].val == p.val+1,
        g[y+1][x].val <= p.val
    ]):
        n.append(g[y+1][x])
    # Down
    if y > 0 and any([
        g[y-1][x].val == p.val+1,
        g[y-1][x].val <= p.val
    ]):
        n.append(g[y-1][x])
    # Left
    if x > 0 and any([
        g[y][x-1].val == p.val+1,
        g[y][x-1].val <= p.val
    ]):
        n.append(g[y][x-1])
    # Right
    if x < len(g[0])-1 and any([
        g[y][x+1].val == p.val+1,
        g[y][x+1].val <= p.val
    ]):
        n.append(g[y][x+1])
    return n


def get_distance(s, e, g):
    distance = {s.pos(): 0}
    current = s
    q = []
    q.append(current)

    while len(q):
        current = q.pop(0)
        dist = distance[current.pos()] + 1

        for n in neighbors(current, g):
            if n.pos() not in distance:
                q.append(n)
                distance[n.pos()] = dist

    if e.pos() in distance:
        return distance[e.pos()]
    return None


def part_one(s, e, g):
    distance = {s.pos(): 0}
    current = s
    q = []
    q.append(current)

    while len(q):
        current = q.pop(0)
        dist = distance[current.pos()] + 1

        for n in neighbors(current, g):
            if n.pos() not in distance:
                q.append(n)
                distance[n.pos()] = dist

    print(distance[e.pos()])


def part_two(s, e, g):
    distances = []
    for r in g:
        for c in r:
            if c.val == s:
                d = get_distance(c, e, g)
                if d:
                    distances.append(d)
        print()

    print(f"{min(distances)}")


def main():
    lines = FileReader.read_lines(Path(__file__).parent.absolute())

    start, end, graph = get_height_map(lines)

    part_one(start, end, graph)
    part_two(lowers.index('a'), end, graph)


if __name__ == "__main__":
    main()
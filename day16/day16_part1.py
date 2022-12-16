import random
from helpers.file_reader import FileReader
from pathlib import Path
import re
from dataclasses import dataclass

@dataclass
class Valve:
    name: str
    flow: int
    adj: list
    closed: bool = True
    def value(self):
        return self.flow if self.closed else 0


def valve_graph(lines):
    valves = {}
    for line in lines:
        v = re.findall("([A-Z]*)[a-z ]*=([\d]*);[a-z ]*([A-Z, ]*)", line)[0]
        valves[v[0]] = Valve(v[0], int(v[1]), [a for a in v[2].split(", ")])

    return valves


def max_value(valves, dist):
    m = None
    for v in dist.keys():
        f = valves[v].flow if valves[v].closed else 0
        if m == None:
            m = (v, f)
        elif f > m[1]:
            m = (v, f)

    return m[0]


def get_best_option(valves, v):
    # print(valves)
    q = [n for n in valves.keys()] 
    # print(q)
    dist = {n: 10**3 for n in q}
    prev = {n: None for n in q}
    dist[v] = 0
    del q[q.index(v)]
    
    while len(q) > 0:
        v = q[q.index(max_value(valves, dist))]
        del q[q.index(v)]
        for n in valves[v].adj:
            d = dist[n]+valves[v].value()
            if d < dist[v]:
                dist[v] = v
                prev[v] = n
    
    return sum([f for f in dist.items()])

def part_one(valves):
    t = 30
    pressure = 0
    # for v in valves.keys():
    #     get_best_option(valves, v)
    get_best_option(valves, "DD")

    while t > 0:
        values = []

        t -= 1

    print(f"{pressure}")


def main():
    lines = FileReader.read_lines(Path(__file__).parent.absolute())
    lines = [
        "Valve AA has flow rate=0; tunnels lead to valves DD, II, BB",
        "Valve BB has flow rate=13; tunnels lead to valves CC, AA",
        "Valve CC has flow rate=2; tunnels lead to valves DD, BB",
        "Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE",
        "Valve EE has flow rate=3; tunnels lead to valves FF, DD",
        "Valve FF has flow rate=0; tunnels lead to valves EE, GG",
        "Valve GG has flow rate=0; tunnels lead to valves FF, HH",
        "Valve HH has flow rate=22; tunnel leads to valve GG",
        "Valve II has flow rate=0; tunnels lead to valves AA, JJ",
        "Valve JJ has flow rate=21; tunnel leads to valve II"
    ]

    valves = valve_graph(lines)
    part_one(valves)


if __name__ == "__main__":
    main()
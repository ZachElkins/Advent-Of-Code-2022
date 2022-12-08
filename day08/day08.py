from helpers.file_reader import FileReader
from pathlib import Path


def part_one(forest):
    w = len(forest)
    h = len(forest[0])
    visible = 2*(w+h)-4

    for i in range(1, w-1):
        for j in range(1, h-1):
            height = forest[i][j]
            vis_l = [forest[k][j] for k in range(0, i)]
            vis_r = [forest[k][j] for k in range(i+1, w)]
            vis_u = [forest[i][k] for k in range(0, j)]
            vis_d = [forest[i][k] for k in range(j+1, h)]
            visible += 1 if sum([
                all([t < height for t in vis_l]),
                all([t < height for t in vis_r]),
                all([t < height for t in vis_u]),
                all([t < height for t in vis_d]),
            ]) >= 1 else 0

    print(f"{visible}")
 

def part_two(forest):
    w = len(forest)
    h = len(forest[0])
    best_view = 0
    
    for i in range(1, w-1):
        for j in range(1, h-1):
            height = forest[i][j]
            vis_l = [forest[k][j] < height for k in range(i-1, -1, -1)]
            vis_r = [forest[k][j] < height for k in range(i+1, w)]
            vis_u = [forest[i][k] < height for k in range(j-1, -1, -1)]
            vis_d = [forest[i][k] < height for k in range(j+1, h)]
            
            view_l = vis_l.index(False)+1 if False in vis_l else len(vis_l)
            view_r = vis_r.index(False)+1 if False in vis_r else len(vis_r)
            view_u = vis_u.index(False)+1 if False in vis_u else len(vis_u)
            view_d = vis_d.index(False)+1 if False in vis_d else len(vis_d)
            
            view = view_l * view_r * view_u * view_d

            if view > best_view: best_view = view

    print(f"{best_view}")


def main():
    forest = FileReader.read_lines(Path(__file__).parent.absolute())

    part_one(forest)
    part_two(forest)


if __name__ == "__main__":
    main()
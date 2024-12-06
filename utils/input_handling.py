def read_grid(in_file) -> dict:
    with open(in_file) as file:
        grid = {(x, y): char for y, row in enumerate(file)
                for x, char in enumerate(row.strip("\n"))}
    return grid


def render_grid(grid):
    xmin, *_, xmax = sorted({x for x, y in grid.keys()})
    ymin, *_, ymax = sorted({y for x, y in grid.keys()})

    print("\n".join("".join(grid.get((x, y), ' ')
                    for x in range(xmin, xmax + 1))
                    for y in range(ymin, ymax + 1)))


def file_lines(in_file):
    with open(in_file) as file:
        for line in file:
            """Custom iteration logic goes here"""
            line = line.strip()
            yield line

TEST = False
in_file = "./resources/day_24_test.txt" if TEST else "./resources/day_24_input.txt"

from collections import deque

def file_lines():
    with open(in_file) as file:
        return [line.strip() for line in file]

        # for line in file:
        #     """Custom iteration logic goes here"""
        #     line = line.strip()
        #     yield line


grid_x = len(file_lines()[0]) - 2
grid_y = len(file_lines()) - 2

storm_dir = {"<": (-1, 0), ">": (1, 0), "^": (0, -1), "v": (0, 1)}


def question_1():
    """Answer to the first question of the day"""
    return bfs((0, -1, 0), (grid_x-1, grid_y-1))

def question_2():
    """Answer to the second question of the day"""
    trip = bfs((0, -1, 0), (grid_x-1, grid_y))
    print(f"First trip {trip}")
    trip = bfs((grid_x-1, grid_y, trip), (0, -1))
    print(f"Second trip {trip}")
    trip = bfs((0, -1, trip), (grid_x-1, grid_y))
    print(f"Third trip {trip}")
    return trip


def init_grid():
    grid = {}
    for y, line in enumerate(file_lines()):
        for x, char in enumerate(line):
            if char not in ["#", "."]:
                grid[(x - 1, y - 1)] = [char]
    return grid


def render_grid(grid):
    # Horrendous
    print("#" * (grid_x + 2), end="")
    print()
    for y in range(grid_y):
        print("#", end="")
        for x in range(grid_x):
            if (x, y) in grid:
                if len(grid[(x, y)]) == 1:
                    print(grid[(x, y)][0], end="")
                else:
                    print(len(grid[(x, y)]), end="")
            else:
                print(".", end="")
        print("#")
    print("#" * (grid_x + 2), end="")
    print()


def transform_grid(grid, dt):
    new_grid = {}
    for storm_location in grid:
        for storm in grid[storm_location]:
            new_location = ((storm_location[0] + storm_dir[storm][0] * dt) % grid_x,
                            (storm_location[1] + storm_dir[storm][1] * dt) % grid_y)
            if new_location in new_grid:
                new_grid[new_location].append(storm)
            else:
                new_grid[new_location] = [storm]
    return new_grid

def grid_neighbors(grid, pos):
    neighbours = []
    grid = transform_grid(grid, pos[2] + 1)
    for step in [(0,0), (0,1), (0,-1), (1,0), (-1,0)]:
        new_pos = (pos[0] + step[0], pos[1] + step[1])
        if new_pos == (0,-1) or new_pos == (grid_x-1,grid_y):
            neighbours.append((*new_pos, pos[2] + 1))
        if new_pos[0] < 0 or new_pos[1] < 0 or new_pos[0] >= grid_x or new_pos[1] >= grid_y:
            continue
        if new_pos not in grid:
            neighbours.append((*new_pos, pos[2] + 1))
    return neighbours

def trace_path(reached, final):
    path = [final]
    current = final
    while reached[current]:
        path.append(reached[current])
        current = reached[current]

    path.reverse()
    for i in path:
        print(i)

def bfs(start, end):
    frontier = []
    frontier.append(start)
    reached = dict()
    reached[start] = None

    while not len(frontier) == 0:
        best = best_element(frontier, end)
        current = frontier.pop(best)
        for neighbour in grid_neighbors(grid, current):
            if neighbour not in reached:
                frontier.append(neighbour)
                reached[neighbour] = current
                # print(neighbour)
                if neighbour[0] == end[0] and neighbour[1] == end[1]:
                    # trace_path(reached, neighbour)
                    return neighbour[2]
    print("No route Found!")
    raise RuntimeError

def best_element(frontier, target):
    # This adds the A* effect to the code. makes the frontier a priority queue
    index = 0
    closeness = float('inf')
    for i, element in enumerate(frontier):
        elx, ely, _ = element
        tx, ty = target
        if (elx-tx)**2 + (ely-ty)**2 < closeness:
            closeness =(elx-tx)**2 + (ely-ty)**2
            index = i

    return index

if __name__ == '__main__':
    grid = init_grid()

    answer_1 = question_1()
    print(f"Question 1 answer is: {answer_1}")

    answer_2 = question_2()
    print(f"Question 2 answer is: {answer_2}")

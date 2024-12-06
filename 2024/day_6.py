TEST = False
in_file = "./resources/day_6_test.txt" if TEST else "./resources/day_6.txt"

from utils.input_handling import read_grid, render_grid
from copy import deepcopy as copy

grid = read_grid(in_file)

DIRS = {(1, 0): ">", (-1, 0): "<", (0, 1):"v", (0, -1): "^"}

def question_1():
    """Answer to the first question of the day"""
    grid = read_grid(in_file)
    start = find_start(grid)
    guard = start

    direction = (0, -1)

    visited = [start]
    while grid.get((guard[0] + direction[0], guard[1] + direction[1])):
        if grid.get((guard[0] + direction[0], guard[1] + direction[1])) == "#":
            direction = turn_right(direction)

        guard = (guard[0] + direction[0], guard[1]+direction[1])
        visited.append(guard)

    return set(visited)


def find_start(grid) -> tuple:
    for key in grid:
        if grid[key] == "^":
            return key

def question_2():
    """Answer to the second question of the day"""
    answer = 0
    grid = read_grid(in_file)
    start = find_start(grid)

    visited = question_1()

    for visit in set(visited):
        new_grid = copy(grid)
        new_grid[visit] = "#"

        if guard_sim(new_grid, start, (0, -1)):
            answer += 1

    return answer


def turn_right(direction) -> tuple:
    x, y = direction
    return -y, x


def guard_sim(grid, guard, direction):
    visited = {}
    while grid.get((guard[0] + direction[0], guard[1]+direction[1])):
        if guard not in visited:
            visited[guard] = [DIRS[direction]]
        else:
            visited[guard].append(DIRS[direction])

        while grid.get((guard[0] + direction[0], guard[1] + direction[1])) == "#":
            direction = (-direction[1], direction[0])

        guard = (guard[0] + direction[0], guard[1]+direction[1])
        grid[guard] = "X"

        if visited.get(guard) and DIRS[direction] in visited.get(guard):
            return True

    return False



if __name__ == '__main__':
    answer_1 = len(question_1())
    print(f"Question 1 answer is: {answer_1}")

    answer_2 = question_2()
    print(f"Question 2 answer is: {answer_2}")
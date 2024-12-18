TEST = False
in_file = "./resources/day_16_test.txt" if TEST else "./resources/day_16.txt"
from utils.input_handling import read_grid, render_grid

grid = read_grid(in_file, ".")
DIRS = ((1, 0), (-1, 0), (0, 1), (0, -1))
states = {}


def question_1():
    """Answer to the first question of the day"""
    start, end = (0,0), (0,0)

    for point in grid:
        if grid[point] == "S":
            start = point
        if grid[point] == "E":
            end = point

    del grid[end]
    visited = []

    front = [(0, start, (1, 0), None)]
    while front:

        best = best_element(front, end)
        score, step, direction, prev = front.pop(best)

        if (score, step) not in states:
            states[(score, step)] = [prev]
        elif prev not in states[(score, step)]:
            states[(score, step)].append(prev)

        visited.append((step, direction))

        if step == end:
            return score

        front += neighbours(score, step, direction, visited)


def neighbours(score, point, straight, visited):
    p_x, p_y = point
    backwards = [-s for s in straight]
    neighbours = []
    for direction in DIRS:
        d_x, d_y = direction
        step = (p_x + d_x, p_y + d_y)
        if not grid.get(step) and (step, direction) not in visited:
            if direction == backwards:
                continue
            if direction == straight:
                neighbours.append((score + 1, step, direction, (score, point)))
            else:
                neighbours.append((score + 1001, step, direction, (score, point)))
        else:
            # allow re-merging paths that are an equivalent score
            if direction == straight and (score+1, step) in states:
                states[score+1, step].append((score, point))
            elif direction != straight and (score+1001, step) in states:
                states[(score+1001, step)].append((score, point))
    return neighbours


def best_element(front, target):
    index = 0
    hyer = float("inf")
    t_x, t_y = target
    for i, element in enumerate(front):
        score, point, direction, _ = element
        p_x, p_y = point
        score += abs(p_x - t_x) + abs(p_y - t_y)
        if p_x == t_x and direction == (0, 1) or p_x == t_x and direction == (0,1):
            pass
        if direction in [(-1, 0), (0, -1)]:
            score += 2000
        else:
            score += 1000
        if score < hyer:
            hyer = score
            index = i
    return index


def question_2():
    """Answer to the second question of the day"""
    path_length = question_1()

    global grid

    grid = read_grid(in_file, ".")

    for point in grid:
        if grid[point] == "S":
            start = point
        if grid[point] == "E":
            end = point

    pointers = states[(path_length, end)]

    answer = 1
    while pointers:
        pointer = pointers.pop()
        if pointer == None:
            continue
        _, point = pointer
        grid[point] = "O"
        pointers += states[pointer]

    render_grid(grid)

    for point in grid.values():
        if point == "O":
            answer += 1

    return path_length, answer



if __name__ == '__main__':

    answer_1, answer_2 = question_2()
    print(f"Question 1 answer is: {answer_1}")
    print(f"Question 2 answer is: {answer_2}")
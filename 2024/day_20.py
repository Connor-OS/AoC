TEST = False
in_file = "./resources/day_20_test.txt" if TEST else "./resources/day_20.txt"
cheat_tol = 50 if TEST else 100
from utils.input_handling import read_grid, render_grid

DIRS = ((1, 0), (-1, 0), (0, 1), (0, -1))

grid = read_grid(in_file, ".")


# render_grid(grid)

def question_1():
    """Answer to the first question of the day"""

    global grid

    answer_1, answer_2 = 0, 0
    start, end = (0, 0), (0, 0)
    for point in grid:
        if grid[point] == "S":
            start = point
        if grid[point] == "E":
            end = point

    del grid[end]

    best_path = bfs(grid, start, end)
    best_path[end] = len(best_path)+1

    # for point in gp:
    #     p_x, p_y = point
    #     for d_x, d_y in DIRS:
    #         step = (p_x + (d_x*2), p_y + (d_y*2))
    #         if step in gp:
    #             cheat = gp[step] - (gp[point]+2)
    #             if cheat >= 100:
    #                 answer_1 += 1

    distances = flood_fill(grid, end)
    distances[start] = len(best_path)-1
    cheats = {}

    cheat_radius = 20
    for point in distances:
        p_x, p_y = point
        for s_x in range(p_x - cheat_radius, p_x + cheat_radius+1):
            x_dist = abs(s_x - p_x)
            for s_y in range(p_y - (cheat_radius - x_dist), p_y + (cheat_radius + 1 - x_dist)):
                step = (s_x, s_y)
                grid[step] = str(abs(s_x - p_x) + abs(s_y - p_y))[-1]
                if step in distances:
                    if cheat := try_cheat(point, step, distances):
                        if cheat in cheats:
                            cheats[cheat] += 1
                        else:
                            cheats[cheat] = 1
                        answer_2 += 1

    for cheat in cheats:
        print(f"{cheats[cheat]} that save {cheat} seconds")

    return answer_2


def try_cheat(start_cheat, end_cheat, distances):
    s_x, s_y = start_cheat
    e_x, e_y = end_cheat

    cheat_dist = abs(e_x - s_x) + abs(e_y - s_y)
    cheat_by = distances[start_cheat] - (distances[end_cheat] + cheat_dist)
    if cheat_by >= cheat_tol:
        return cheat_by

def bfs(grid, start, end):
    visited = []
    front = [(start, 0)]
    states = {start: None}

    while front:
        point, score = front.pop()

        if point == end:
            return golden_path(states, end, score)

        visited.append(point)

        p_x, p_y = point
        for d_x, d_y in DIRS:
            step = (p_x + d_x, p_y + d_y)
            if step not in grid and step not in visited:
                front.append((step, score+1))
                states[step] = point
    return 0

def flood_fill(grid, start):
    visited = []
    front = [(start, 0)]
    distances = {start: 0}

    while front:
        point, score = front.pop()

        visited.append(point)

        p_x, p_y = point
        for d_x, d_y in DIRS:
            step = (p_x + d_x, p_y + d_y)
            if step not in grid and step not in visited:
                front.append((step, score+1))
                distances[step] = score+1
    return distances

def golden_path(path, end, score):
    score -= 1
    pointer = path[end]
    golden_path = {pointer: score}
    while pointer:
        pointer = path[pointer]

        if pointer:
            golden_path[pointer] = score
            score -= 1

    return golden_path


def question_2():
    """Answer to the second question of the day"""
    answer = 0

    return answer


if __name__ == '__main__':
    answer_1 = question_1()
    print(f"Question 1 answer is: {answer_1}")

    # answer_2 = question_2()
    # print(f"Question 2 answer is: {answer_2}")
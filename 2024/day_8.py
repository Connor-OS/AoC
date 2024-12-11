TEST = False

in_file = "./resources/day_8_test.txt" if TEST else "./resources/day_8.txt"

from utils.input_handling import read_grid,render_grid

grid = read_grid(in_file)

def question_1():
    """Answer to the first question of the day"""
    answer = 0
    global grid

    aintinodes = []

    visited = []

    for point in grid:
        if grid[point] not in visited + [".", "#"]:
            char = grid[point]
            visited += char

            aintinodes += compute_antinodes(char)

    # render_grid(grid)

    return len(set(aintinodes))


def compute_antinodes(char):
    aintinodes = []
    for p in grid:
        if grid[p] == char:
            for q in grid:
                if grid[q] == char and p != q:
                    p_x, p_y = p
                    q_x, q_y = q
                    d_x, d_y = q_x-p_x, q_y-p_y

                    node  = (p_x - d_x, p_y- d_y)
                    if grid.get(node):
                        aintinodes.append(node)

    print(aintinodes)
    return aintinodes

def compute_antinodes_2(char):
    aintinodes = []
    for p in grid:
        if grid[p] == char:
            for q in grid:
                if grid[q] == char and p != q:
                    p_x, p_y = p
                    q_x, q_y = q
                    d_x, d_y = q_x-p_x, q_y-p_y

                    potential_node = (p_x - d_x, p_y - d_y)

                    while grid.get(potential_node):
                        aintinodes.append(potential_node)
                        pot_x, pot_y = potential_node
                        potential_node = (pot_x - d_x, pot_y - d_y)

                    potential_node = (p_x + d_x, p_y + d_y)

                    while grid.get(potential_node):
                        aintinodes.append(potential_node)
                        pot_x, pot_y = potential_node
                        potential_node = (pot_x + d_x, pot_y + d_y)

    return aintinodes


def question_2():
    """Answer to the second question of the day"""
    answer = 0
    global grid

    aintinodes = []

    visited = []

    for point in grid:
        if grid[point] not in visited + [".", "#"]:
            char = grid[point]
            visited += char

            aintinodes += compute_antinodes_2(char)

    render_grid(grid)

    return len(set(aintinodes))


if __name__ == '__main__':
    # answer_1 = question_1()
    # print(f"Question 1 answer is: {answer_1}")

    answer_2 = question_2()
    print(f"Question 2 answer is: {answer_2}")
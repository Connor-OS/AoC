TEST = False
in_file = "./resources/day_15_test.txt" if TEST else "./resources/day_15.txt"
from utils.input_handling import render_grid


DIRS = {">": (1, 0), "<": (-1, 0), "v": (0, 1), "^": (0, -1)}
def file_lines():
    with open(in_file) as file:
        grid, moves = file.read().split("\n\n")
        grid = {(x, y): char for y, row in enumerate(grid.split("\n"))
                for x, char in enumerate(row) if char != "."}
        moves = [move for move in moves if move != "\n"]
        return grid, moves

def convert_map(grid):
    new_grid = {}
    for point in grid:
        char = grid[point]
        p_x, p_y = point
        if char == "O":
            new_grid[(p_x*2, p_y)] = "["
            new_grid[(p_x*2+1, p_y)] = "]"
        else:
            new_grid[(p_x*2, p_y)] = char
            if char != "@":
                new_grid[(p_x*2+1, p_y)] = char
    return new_grid

def question_1():
    """Answer to the first question of the day"""
    answer = 0
    grid, moves = file_lines()
    robot = (0, 0)
    for point in grid:
        if grid[point] == "@":
            robot = point

    for move in moves:
        m_x, m_y = DIRS[move]
        r_x, r_y = robot
        step = (r_x + m_x, r_y+m_y)
        push = step

        while grid.get(push):
            if grid[push] == "#":
                break
            p_x, p_y = push
            push = (p_x + m_x, p_y+m_y)
        else:
            grid[push] = "O"
            grid[step] = "@"
            del grid[robot]
            robot = step

    for p_x, p_y in grid:
        if grid[(p_x, p_y)] == "O":
            answer += p_x + 100*p_y

    return answer


def question_2():
    """Answer to the second question of the day"""
    answer = 0
    grid, moves = file_lines()
    grid = convert_map(grid)

    robot = (0, 0)
    for point in grid:
        if grid[point] == "@":
            robot = point


    for move in moves:
        m_x, m_y = DIRS[move]
        r_x, r_y = robot
        step = (r_x + m_x, r_y+m_y)
        push_face = [robot]
        push_chain = []
        while push_face:
            push = push_face.pop()

            if grid.get(push) == "#":
                break
            if not grid.get(push):
                continue


            push_chain.append(push)
            p_x, p_y = push
            push = (p_x + m_x, p_y+m_y)

            push_face.append(push)
            if move in ["v", "^"]:
                if grid.get(push) == "[" and (p_x + m_x + 1, p_y+m_y) not in push_face:
                    push_face.append((p_x + m_x + 1, p_y+m_y))
                if grid.get(push) == "]" and (p_x + m_x - 1, p_y+m_y) not in push_face:
                    push_face.append((p_x + m_x - 1, p_y+m_y))
        else:
            push_chain.reverse()
            visited = []
            for p_x, p_y in push_chain:
                if (p_x, p_y) in visited:
                    continue
                char = grid[(p_x, p_y)]
                push = (p_x + m_x, p_y+m_y)
                grid[push] = char
                del grid[(p_x, p_y)]
                visited.append((p_x, p_y))
            grid[step] = "@"
            robot = step

        print("=================================")
        render_grid(grid)

    for p_x, p_y in grid:
        if grid[(p_x, p_y)] == "[":
            answer += p_x + 100*p_y

    return answer


if __name__ == '__main__':
    answer_1 = question_1()
    print(f"Question 1 answer is: {answer_1}")

    answer_2 = question_2()
    print(f"Question 2 answer is: {answer_2}")
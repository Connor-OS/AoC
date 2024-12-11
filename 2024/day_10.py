TEST = False
in_file = "./resources/day_10_test.txt" if TEST else "./resources/day_10.txt"

from utils.input_handling import read_int_grid
from collections import deque

grid = read_int_grid(in_file)
DIRS = {(1, 0): "r", (-1, 0): "l", (0, 1): "d", (0, -1): "u"}

def question_1():
    """Answer to the first question of the day"""
    answer = 0
    global grid

    for head in grid:
        if grid[head] == 0:
            answer += compute_trail_cost(head)

    return answer

def compute_trail_cost(head):
    score = 0
    front = deque(neighbours(*head))
    visited = []
    while front:
        neighbour = front.popleft()
        # if neighbour in visited:
        #     continue
        visited.append(neighbour)
        if grid[neighbour] == 9:
            score += 1
            continue
        front += neighbours(*neighbour)

    return score


def neighbours(x, y):
    neighbours = []
    for d_x, d_y in DIRS:
        neighbour = (x+d_x, y+d_y)
        if neighbour in grid and grid[neighbour] == grid[(x,y)] + 1:
            neighbours.append(neighbour)

    return neighbours

def question_2():
    """Answer to the second question of the day"""
    answer = None

    return answer


if __name__ == '__main__':
    answer_1 = question_1()
    print(f"Question 1 answer is: {answer_1}")

    # answer_2 = question_2()
    # print(f"Question 2 answer is: {answer_2}")
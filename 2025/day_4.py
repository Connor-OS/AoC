TEST = False
in_file = "./resources/day_4_test.txt" if TEST else "./resources/day_4.txt"

from utils.input_handling import read_grid

def remove_from_grid(grid: dict) -> (dict, int):
    removed = []
    for sx, sy in grid:
        if grid.get((sx, sy)) != "@":
            continue
        adjacent = 0
        directions = [(1,0), (1,1), (0,1), (-1,1), (-1,0), (-1,-1), (0,-1), (1,-1)]
        for dx, dy in directions:
            if grid.get((sx+dx, sy+dy)) == "@":
                adjacent += 1

        if adjacent < 4:
            removed.append((sx, sy))

    grid = {key:val for key, val in grid.items() if key not in removed}

    return grid, len(removed)


def question_1():
    """Answer to the first question of the day"""
    answer = 0

    grid = read_grid(in_file)
    grid, removed = remove_from_grid(grid)

    return removed


def question_2():
    """Answer to the second question of the day"""
    grid = read_grid(in_file)
    grid, removed = remove_from_grid(grid)
    answer = removed

    while removed > 0:
        grid, removed = remove_from_grid(grid)
        answer += removed

    return answer


if __name__ == '__main__':
    answer_1 = question_1()
    print(f"Question 1 answer is: {answer_1}")

    answer_2 = question_2()
    print(f"Question 2 answer is: {answer_2}")

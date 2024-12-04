TEST = False
in_file = "./resources/day_4_test.txt" if TEST else "./resources/day_4.txt"

with open(in_file) as file:
    grid = {(x, y): char for y, row in enumerate(file)
            for x, char in enumerate(row.strip("\n"))}


def valid_xmas(x, y):
    MAS = ["M", "A", "S"]
    valid = 0

    directions = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1)]

    for x_dir, y_dir in directions:
        if MAS == [grid.get((x + x_dir * (i + 1),
                             y + y_dir * (i + 1)))
                   for i, char in enumerate(MAS)]:
            valid += 1

    return valid


def valid_xmas_2(x, y):
    MAS = ["M", "A", "S"]
    valid = 0

    directions = [(1, 1), (-1, -1), (-1, 1), (1, -1)]

    for x_dir, y_dir in directions:
        if MAS == [grid.get((x + x_dir * (i - 1),
                             y + y_dir * (i - 1)))
                   for i, char in enumerate(MAS)]:
            valid += 1

    return valid > 1


def question_1():
    """Answer to the first question of the day"""
    answer = 0
    for x, y in grid:
        if grid[x, y] == "X":
            answer += valid_xmas(x, y)

    return answer


def question_2():
    """Answer to the second question of the day"""
    answer = 0
    for x, y in grid:
        if grid[x, y] == "A":
            answer += valid_xmas_2(x, y)

    return answer


if __name__ == '__main__':
    answer_1 = question_1()
    print(f"Question 1 answer is: {answer_1}")

    answer_2 = question_2()
    print(f"Question 2 answer is: {answer_2}")

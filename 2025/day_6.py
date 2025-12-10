TEST = False
in_file = "./resources/day_6_test.txt" if TEST else "./resources/day_6.txt"

from utils.input_handling import file_lines
from utils.input_handling import read_grid, render_grid

def question_1():
    """Answer to the first question of the day"""
    answer = 0
    numbers = []
    operators = []
    for line in file_lines(in_file):
        try:
            numbers.append([int(n) for n in line.split()])
        except:
            operators = [o.strip() for o in line.split()]


    for i, operator in enumerate(operators):
        if operator == "*":
            result = 1
            for row in numbers:
                result *= row[i]
        else:
            result = 0
            for row in numbers:
                result += row[i]

        answer += result
    return answer


def process_nums(numbers, operator):
    if operator == "*":
        result = 1
        for num in numbers:
            result *= int(num)
    else:
        result = 0
        for num in numbers:
            result += int(num)
    return result

def question_2():
    """Answer to the second question of the day"""
    answer = 0

    grid = read_grid(in_file)
    render_grid(grid)


    with open(in_file) as f:
        lines = f.readlines()
        height, width = len(lines), len(lines[0])

    operator = "*"
    numbers = []
    for col in range(width):
        operator = grid.get((col, height-1)) if grid.get((col, height-1)) != " " else operator

        number = ""
        for row in range(height - 1):
            num = grid.get((col, row))
            if num and num != " ":
                number += num

        if number:
            numbers.append(number)
        else:
            answer += process_nums(numbers, operator)
            numbers = []

    answer += process_nums(numbers, operator)

    return answer


if __name__ == '__main__':
    answer_1 = question_1()
    print(f"Question 1 answer is: {answer_1}")

    answer_2 = question_2()
    print(f"Question 2 answer is: {answer_2}")

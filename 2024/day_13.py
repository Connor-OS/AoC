TEST = False
in_file = "./resources/day_13_test.txt" if TEST else "./resources/day_13.txt"

import string
import re
import numpy as np


def file_lines():
    with open(in_file) as file:
        for section in file.read().split("\n\n"):
            yield [[int(i) for i in re.findall('\d+', line)] for line in section.splitlines()]


def question_1():
    """Answer to the first question of the day"""
    answer = 0
    for line in file_lines():
        equation_1, equation_2, result = line

        array = np.array([equation_1, equation_2]).transpose()

        x, y = np.linalg.solve(array, result)
        x, y = round(x), round(y)

        if all(np.dot(array, np.array([x, y])) == result) and x <= 100 and y <= 100:
            answer += (3 * x) + y

    return answer


def question_2():
    """Answer to the second question of the day"""
    answer = 0
    for line in file_lines():
        equation_1, equation_2, result = line

        result = [i+10000000000000 for i in result]

        array = np.array([equation_1, equation_2]).transpose()

        x, y = np.linalg.solve(array, result)
        x, y = round(x), round(y)

        if all(np.dot(array, np.array([x, y])) == result) :
            answer += (3 * x) + y

    return answer


if __name__ == '__main__':
    answer_1 = question_1()
    print(f"Question 1 answer is: {answer_1}")

    answer_2 = question_2()
    print(f"Question 2 answer is: {answer_2}")

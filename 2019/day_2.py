TEST = False
in_file = "./resources/day_2_test.txt" if TEST else "./resources/day_2.txt"

from utils.input_handling import file_lines
from itertools import islice

from incode_computer import IntcodeComputer

def question_1(a,b):
    """Answer to the first question of the day"""

    with open(in_file) as file:
        instructions = file.read().split(',')
    instructions = [int(i) for i in instructions]

    instructions[1] = a
    instructions[2] = b

    computer = IntcodeComputer(instructions)
    return computer.execute()


def question_2():
    """Answer to the second question of the day"""
    answer = 0

    for a in range(99):
        for b in range(99):
            if question_1(a,b) == 19690720:
                return 100 * a + b

    return answer


if __name__ == '__main__':
    answer_1 = question_1(12, 2)
    print(f"Question 1 answer is: {answer_1}")

    answer_2 = question_2()
    print(f"Question 2 answer is: {answer_2}")

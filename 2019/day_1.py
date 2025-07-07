TEST = False
in_file = "./resources/day_1_test.txt" if TEST else "./resources/day_1.txt"

from utils.input_handling import file_lines
from math import floor

def question_1():
    """Answer to the first question of the day"""
    answer = 0
    for line in file_lines(in_file):
        answer += fuel_required(int(line))

    return answer

def fuel_required(mass):
    return floor(mass / 3) - 2

def question_2():
    """Answer to the second question of the day"""
    answer = 0
    for line in file_lines(in_file):
        fuel = fuel_required(int(line))
        answer += fuel
        while fuel > 0:
            fuel = fuel_required(fuel)
            if fuel > 0:
                answer += fuel

    return answer

if __name__ == '__main__':
    answer_1 = question_1()
    print(f"Question 1 answer is: {answer_1}")

    answer_2 = question_2()
    print(f"Question 2 answer is: {answer_2}")

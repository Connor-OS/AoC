TEST = False
in_file = "./resources/day_10_test.txt" if TEST else "./resources/day_10.txt"

from utils.input_handling import file_lines
from z3 import *

def process_input(line):
    line = line.split()
    lights, buttons, joltage = line[0], line[1:-1], line[-1]
    lights = lights.strip("[]")
    lights = lights.replace(".", "0").replace("#", "1")
    lights = [int(l) for l in lights]

    buttons = [[int(n) for n in button.strip("()").split(",")] for button in buttons]

    joltage = [int(j) for j in joltage.strip("{}").split(",")]

    return lights, buttons, joltage

def question_1():
    """Answer to the first question of the day"""
    answer = 0

    for line in file_lines(in_file):
        lights, buttons, _ = process_input(line)
        answer += bfs(lights, buttons)

    return answer

def bfs(target_lights, buttons):

    front = [(0, [0] * len(target_lights))]

    while True:
        state = front.pop(0)
        for button in buttons:
            lights = [i for i in state[1]]
            for wire in button:
                if lights[wire] == 0:
                    lights[wire] = 1
                else:
                    lights[wire] = 0
            if lights == target_lights:
                return state[0] + 1
            front.append((state[0] + 1, lights))


def question_2():
    """Answer to the second question of the day"""
    answer = 0
    # Z3 to the Rescue!!

    for line in file_lines(in_file):
        _, buttons, joltage = process_input(line)

        vars = [Int(f"x{i}") for i, _ in enumerate(buttons)]

        opt = Optimize()
        for i, jolts in enumerate(joltage):
            opt.add(sum([var for var, button in zip(vars, buttons) if i in button]) == jolts)

        for var in vars:
            opt.add(var >= 0)

        # objective
        h1 = opt.minimize(sum(vars))

        opt.check()
        answer += opt.lower(h1).as_long()

    return answer


if __name__ == '__main__':
    answer_1 = question_1()
    print(f"Question 1 answer is: {answer_1}")

    answer_2 = question_2()
    print(f"Question 2 answer is: {answer_2}")

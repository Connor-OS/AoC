TEST = False
in_file = "./resources/day_17_test.txt" if TEST else "./resources/day_17.txt"
import re
import pandas as pd


with open(in_file) as file:
    registers, program = file.read().split("\n\n")
    registers = [int(i) for i in re.findall("-?\d+", registers)]
    program = [int(i) for i in re.findall("-?\d+", program)]


def question_1():
    """Answer to the first question of the day"""
    answer = 0
    global registers, program

    pointer = 0
    out = []
    while pointer < len(program):
        instruction = program[pointer]
        operand = program[pointer+1]
        match instruction:
            case 0:
                registers[0] = int(registers[0] / 2**combo_operand(operand))
            case 1:
                registers[1] = registers[1] ^ operand
            case 2:
                registers[1] = combo_operand(operand) % 8
            case 3:
                if registers[0] == 0:
                    pass
                else:
                    pointer = operand-2
            case 4:
                registers[1] = registers[1] ^ registers[2]
            case 5:
                out.append(combo_operand(operand) % 8)
            case 6:
                registers[1] = int(registers[0] / 2**combo_operand(operand))
            case 7:
                registers[2] = int(registers[0] / 2**combo_operand(operand))

        pointer += 2

    return out


def combo_operand(operand):
    if operand < 4:
        return operand
    return registers[operand-4]


def question_2():
    """Answer to the second question of the day"""
    # Tuned to my specific input file, doesn't work on examples/ may not for other input files

    global registers, program
    register_cache = registers

    pointer = 8**15
    while True:
        registers = register_cache
        registers[0] = pointer
        result = question_1()
        matching_index = 0
        for r, p in zip(reversed(result), reversed(program)):
            if r == p:
                matching_index += 1
            else:
                break
        if matching_index == 16:
            return pointer

        pointer += 8**(15-matching_index)


if __name__ == '__main__':
    answer_1 = question_1()
    print(f"Question 1 answer is: {",".join([str(i) for i in answer_1])}")

    answer_2 = question_2()
    print(f"Question 2 answer is: {answer_2}")
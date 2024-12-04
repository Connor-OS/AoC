TEST = False
in_file = "./resources/day_5_test.txt" if TEST else "./resources/day_5_input.txt"


with open(in_file) as file:
    lines = [line for line in file]

def question_1():
    """Answer to the first question of the day"""
    answer = ""

    stacks = []
    up_to = construct_stack(stacks)

    instructions = []
    for line in lines[up_to + 2:]:
        instruction = line.split()
        instructions.append([int(i)-1 for i in instruction[1:6:2]])

    for instruction in instructions:
        move, fro, to = instruction
        for _ in range(move+1):
            stacks[to].append(stacks[fro].pop())

    for stack in stacks:
        answer += stack[-1]

    return answer


def construct_stack(stacks):
    for line_num, line in enumerate(lines):
        stack = line[1:len(line):4]
        for i, letter in enumerate(stack):
            if stack.isnumeric():
                for s in stacks:
                    s.reverse()
                return line_num
            if len(stacks) < i+1:
                stacks.append([])
            if letter != " ":
                stacks[i].append(letter)

def question_2():
    """Answer to the second question of the day"""
    answer = ""

    stacks = []
    up_to = construct_stack(stacks)

    instructions = []
    for line in lines[up_to + 2:]:
        instruction = line.split()
        instructions.append([int(i)-1 for i in instruction[1:6:2]])

    for instruction in instructions:
        move, fro, to = instruction
        temp = []
        for _ in range(move+1):
            temp.append(stacks[fro].pop())
        temp.reverse()
        stacks[to] += temp

    for stack in stacks:
        answer += stack[-1]

    return answer



if __name__ == '__main__':
    answer_1 = question_1()
    print(f"Question 1 answer is: {answer_1}")

    answer_2 = question_2()
    print(f"Question 2 answer is: {answer_2}")
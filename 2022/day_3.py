import string

TEST = False
in_file = "./resources/day_3_test.txt" if TEST else "./resources/day_3_input.txt"


def file_lines():
    with open(in_file) as file:
        for line in file:
            """Custom iteration logic goes here"""
            line = line.strip()
            yield line


def question_1():
    """Answer to the first question of the day"""
    answer = 0
    for line in file_lines():
        half = int(len(line)/2)
        val = compare(line[0:half], line[half:])
        answer += value(val)
    return answer


def compare(f: string, s: string):
    for i in f:
        if i in s:
            return i

def compare_three(f: string, s: string):
    for i in f:
        if i in s:
            return i


def value(val: string):
    val = ord(val)

    if val > 96:
        val -= 96
    else:
        val -= 38
    return val




def question_2():
    """Answer to the second question of the day"""
    answer = 0

    lines = [line for line in file_lines()]
    for line in range(0,len(lines), 3):
        group = lines[line: line+3]
        for char in group[0]:
            if char in group[1] and char in group[2]:
                answer += value(char)
                break


    return answer


if __name__ == '__main__':
    # answer_1 = question_1()
    # print(f"Question 1 answer is: {answer_1}")

    answer_2 = question_2()
    print(f"Question 2 answer is: {answer_2}")
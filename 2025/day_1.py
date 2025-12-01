TEST = False
in_file = "./resources/day_1_test.txt" if TEST else "./resources/day_1.txt"

from utils.input_handling import file_lines

def question_1():
    """Answer to the first question of the day"""
    answer = 0
    dial = 50

    for line in file_lines(in_file):
        d, clicks = line[0], int(line[1:])
        if d == "L": clicks = -clicks

        dial += clicks
        dial = dial % 100

        if dial == 0: answer += 1

    return answer


def question_2():
    """Answer to the second question of the day"""
    answer = 0
    dial = 50

    for line in file_lines(in_file):
        init_dial = dial
        d, clicks = line[0], int(line[1:])

        turns = int(clicks / 100)
        answer += turns
        clicks = clicks % 100

        if d == "L": clicks = -clicks

        dial += clicks
        dial = dial % 100

        if init_dial == 0: continue

        if d == "L" and (init_dial < dial or dial == 0):
            answer += 1
        elif d == "R" and init_dial > dial:
            answer += 1

    return answer


if __name__ == '__main__':
    answer_1 = question_1()
    print(f"Question 1 answer is: {answer_1}")

    answer_2 = question_2()
    print(f"Question 2 answer is: {answer_2}")

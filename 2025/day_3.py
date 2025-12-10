TEST = False
in_file = "./resources/day_3_test.txt" if TEST else "./resources/day_3.txt"

from utils.input_handling import file_lines

def question_1():
    """Answer to the first question of the day"""
    answer = 0

    for line in file_lines(in_file):
        batteries = [b for b in line]
        batteries.reverse()

        max_joltage = int(batteries[1] + batteries[0])
        for i_1, j_1 in enumerate(batteries[1:]):
            for i_2, j_2 in enumerate(batteries[:i_1+1]):

                if int(j_1 + j_2) > max_joltage:
                    max_joltage = int(j_1 + j_2)

        answer += max_joltage

    return answer


def question_2():
    """Answer to the second question of the day"""
    answer = 0
    for line in file_lines(in_file):
        batteries = [b for b in line]
        batteries.reverse()
        max_joltage = ""

        range_end = len(batteries)
        digits = 12
        for digit in range(digits):
            range_start = digits-(digit+1)
            joltage = -1
            for i, j in enumerate(batteries[range_start:range_end]):
                if int(j) >= joltage:
                    joltage = int(j)
                    range_end = i + (digits-(digit+1))

            max_joltage += str(joltage)

        answer += int(max_joltage)

    return answer


if __name__ == '__main__':
    answer_1 = question_1()
    print(f"Question 1 answer is: {answer_1}")

    answer_2 = question_2()
    print(f"Question 2 answer is: {answer_2}")

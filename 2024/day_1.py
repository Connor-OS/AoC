TEST = False
in_file = "./resources/day_1_test.txt" if TEST else "./resources/day_1.txt"


def file_lines():
    data = [*map(int, open(in_file).read().split())]
    return data[0::2], data[1::2]

def question_1():
    """Answer to the first question of the day"""
    answer = 0
    left, right = file_lines()

    left.sort()
    right.sort()

    for l, r in zip(left, right):
        answer += abs(r-l)

    return answer


def question_2():
    """Answer to the second question of the day"""
    answer = 0

    left, right = file_lines()

    for l in left:
        num = 0
        for r in right:
            if l == r:
                num += 1
        answer += num*l

    return answer


if __name__ == '__main__':
    answer_1 = question_1()
    print(f"Question 1 answer is: {answer_1}")

    answer_2 = question_2()
    print(f"Question 2 answer is: {answer_2}")

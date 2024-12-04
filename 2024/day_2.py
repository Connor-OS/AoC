TEST = False
in_file = "./resources/day_2_test.txt" if TEST else "./resources/day_2.txt"


def file_lines():
    with open(in_file) as file:
        for line in file:
            """Custom iteration logic goes here"""
            yield [int(i) for i in line.split()]

def is_safe(line):
    if line not in [sorted(line), sorted(line)[::-1]]:
        return False

    pairs = zip(*(iter(line[i: ]) for i in range(2)))

    for a,b in pairs:
        if abs(a-b) not in [1, 2, 3]:
            return False

    return True


def question_1():
    """Answer to the first question of the day"""
    return sum([is_safe(l) for l in file_lines()])


def question_2():
    """Answer to the second question of the day"""
    answer = 0

    unsafe_lines = []
    for line in file_lines():

        if is_safe(line):
            answer += 1
        else:
            unsafe_lines.append(line)


    for line in unsafe_lines:
        if any(is_safe(line[: i] + line[i+1::]) for i in range(len(line))):
            answer += 1

    return answer


if __name__ == '__main__':
    answer_1 = question_1()
    print(f"Question 1 answer is: {answer_1}")

    answer_2 = question_2()
    print(f"Question 2 answer is: {answer_2}")
TEST = False
in_file = "./resources/day_7_test.txt" if TEST else "./resources/day_7.txt"

def file_lines():
    with open(in_file) as file:
        for line in file:
            """Custom iteration logic goes here"""
            line = line.strip()

            target, values = line.split(":")

            yield int(target), [int(val) for val in values.split()]


def question_1():
    """Answer to the first question of the day"""
    answer = 0
    for target, values in file_lines():
        values.reverse()
        num = values.pop()
        scores = [num]
        while values:
            new_scores = []
            on = values.pop()
            for score in scores:
                new_scores += [score + on, score * on]
            scores = new_scores

        if target in scores:
            answer += target

    return answer


def question_2():
    """Answer to the second question of the day"""
    answer = 0
    for target, values in file_lines():
        values.reverse()
        num = values.pop()
        scores = [num]
        while values:
            new_scores = []
            on = values.pop()
            for score in scores:
                new_scores += [score + on, score * on, int(str(score) + str(on))]
            scores = new_scores

        if target in scores:
            answer += target

    return answer


if __name__ == '__main__':
    answer_1 = question_1()
    print(f"Question 1 answer is: {answer_1}")

    answer_2 = question_2()
    print(f"Question 2 answer is: {answer_2}")
from copy import deepcopy

TEST = False
in_file = "./resources/day_20_test.txt" if TEST else "./resources/day_20_input.txt"


def file_lines():
    with open(in_file) as file:
        return [int(line) for line in file]


def question_1():
    """Answer to the first question of the day"""
    answer = 0
    sequence = [(i, line) for i, line in enumerate(file_lines())]
    original = deepcopy(sequence)

    for i in original:
        index = sequence.index(i)
        sequence.remove(i)
        moves = i[1]
        new_index = (index + moves) % len(sequence)
        if new_index == 0:
            new_index = len(sequence)
        sequence.insert(new_index, i)

    sequence = [i[1] for i in sequence]

    for i in range(3):
        answer += sequence[(sequence.index(0) + 1000 * (i+1)) % len(sequence)]
    return answer


def question_2():
    """Answer to the second question of the day"""
    answer = 0
    decription_key = 811589153
    sequence = [(i, line * decription_key) for i, line in enumerate(file_lines())]
    original = deepcopy(sequence)
    for j in range(10):
        for i in original:
            index = sequence.index(i)
            sequence.remove(i)
            moves = i[1]
            new_index = (index + moves) % len(sequence)
            if new_index == 0:
                new_index = len(sequence)
            sequence.insert(new_index, i)

    sequence = [i[1] for i in sequence]

    for i in range(3):
        print(sequence[(sequence.index(0) + 1000 * (i+1)) % len(sequence)])
        answer += sequence[(sequence.index(0) + 1000 * (i+1)) % len(sequence)]
    return answer

    return answer


if __name__ == '__main__':
    answer_1 = question_1()
    print(f"Question 1 answer is: {answer_1}")

    answer_2 = question_2()
    print(f"Question 2 answer is: {answer_2}")

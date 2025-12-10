TEST = False
in_file = "./resources/day_5_test.txt" if TEST else "./resources/day_5.txt"

from utils.input_handling import file_lines

def get_ranges_and_ids():
    lines = file_lines(in_file)
    _ranges = []

    while line := next(lines):
        _ranges.append(line)

    ranges = []
    for r in _ranges:
        i, j = r.split("-")
        ranges.append((int(i), int(j)))

    ids = []
    while line := next(lines):
        ids.append(int(line))

    return ranges, ids

def is_fresh(id, ranges):
    for r in ranges:
        if r[0] <= id <= r[1]:
            return True
    return False

def question_1():
    """Answer to the first question of the day"""
    answer = 0

    ranges, ids = get_ranges_and_ids()

    for id in ids:
        if is_fresh(id, ranges):
            answer += 1

    return answer


def question_2():
    """Answer to the second question of the day"""
    answer = 0

    ranges, _ = get_ranges_and_ids()

    ranges = sorted(ranges, key=lambda r: r[0])

    index = 0
    while index < len(ranges)-1:
        if ranges[index][1] +1 >= ranges[index+1][0]:
            if ranges[index][1] < ranges[index+1][1]:
                ranges[index] = (ranges[index][0], ranges[index+1][1])
            ranges.pop(index +1)
        else:
            index += 1

    for r0, r1 in ranges:
        print(r0, r1)
        answer += r1-r0 + 1


    print(len(ranges))

    return answer


if __name__ == '__main__':
    answer_1 = question_1()
    print(f"Question 1 answer is: {answer_1}")

    answer_2 = question_2()
    print(f"Question 2 answer is: {answer_2}")

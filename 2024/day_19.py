TEST = False
in_file = "./resources/day_19_test.txt" if TEST else "./resources/day_19.txt"
from functools import cache

towels = []


def file_lines():
    with open(in_file) as file:
        global towels
        towels, patterns = file.read().split("\n\n")
        towels = towels.split(", ")
        patterns = patterns.split("\n")
        return patterns


def question_1():
    """Answer to the first question of the day"""
    answer = 0

    patterns = file_lines()
    for pattern in patterns:
        if towel_match(pattern):
            answer += 1

    return answer


@cache
def towel_match(pattern):
    if pattern == "":
        return True

    for towel in towels:
        if len(towel) > len(pattern): continue

        if pattern[-len(towel):] == towel:
            if towel_match(pattern[:-len(towel)]):
                return True
    return False


@cache
def towel_match_count(pattern):
    count = 0
    if pattern == "":
        return 1

    for towel in towels:
        if len(towel) > len(pattern): continue

        if pattern[-len(towel):] == towel:
            count += towel_match_count(pattern[:-len(towel)])
    return count

def question_2():
    """Answer to the second question of the day"""
    answer = 0

    patterns = file_lines()
    for pattern in patterns:
        answer += towel_match_count(pattern)

    return answer


if __name__ == '__main__':
    answer_1 = question_1()
    print(f"Question 1 answer is: {answer_1}")

    answer_2 = question_2()
    print(f"Question 2 answer is: {answer_2}")
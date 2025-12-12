from functools import total_ordering

TEST = False
in_file = "./resources/day_12_test.txt" if TEST else "./resources/day_12.txt"


def parse_input():
    with open(in_file) as f:
        lines = f.read().split("\n\n")
        regions, pres = lines[-1], lines[:-1]

    presents = []
    for present in pres:
        present = present[3:].split("\n")
        p = {}
        for i, row in enumerate(present):
            for j, box in enumerate(row):
                if box == "#":
                    p[(i, j)] = "#"

        presents.append(p)

    region_list = []
    regions = regions.split("\n")
    for region in regions:
        region = region.split(":")
        space = region[0].split("x")
        space = (int(space[0]), int(space[1]))

        requirement = [int(r) for r in region[1].split()]

        region_list.append((space, requirement))

    return region_list, presents


def question_1():
    """Answer to the first question of the day"""
    answer = 0

    regions, presents = parse_input()

    i = 1
    for size, requirements in regions:

        total = 0
        for i, requirement in enumerate(requirements):
            total += requirement * len(presents[i])

        if total <= size[0] * size[1]:
            answer += 1

    return answer


if __name__ == '__main__':
    answer_1 = question_1()
    print(f"Question 1 answer is: {answer_1}")

TEST = False
in_file = "./resources/day_10_test.txt" if TEST else "./resources/day_10_input.txt"


def file_lines():
    with open(in_file) as file:
        for line in file:
            """Custom iteration logic goes here"""
            line = line.strip()
            yield line


def question_1():
    """Answer to the first question of the day"""
    answer = 0

    X = 1
    cycle = 0
    for line in file_lines():
        if line == "noop":
            cycle += 1
            if (cycle-20)%40 == 0:
                print(f"{cycle}: {X}")
                answer += X*cycle
        if line.startswith("addx"):
            for i in range(2):
                cycle += 1
                if (cycle-20)%40 == 0:
                    print(f"{cycle}: {X}")
                    answer += X*cycle

            X += int(line.split()[1])



    return answer


def question_2():
    """Answer to the second question of the day"""
    """Answer to the first question of the day"""
    answer = 0

    X = 1
    cycle = 0
    for line in file_lines():
        if line == "noop":
            process_cycle(cycle,X)
            cycle += 1
        if line.startswith("addx"):
            for i in range(2):
                process_cycle(cycle,X)
                cycle += 1

            X += int(line.split()[1])


    return answer

def process_cycle(cycle, X):
    pixel = cycle%40
    if (pixel-2 < X < pixel +2):
        print("#", end="")
    else:
        print(" ", end="")
    if (cycle+1)%40 == 0 and cycle > 0:
        print(cycle)


if __name__ == '__main__':
    # answer_1 = question_1()
    # print(f"Question 1 answer is: {answer_1}")

    answer_2 = question_2()
    print(f"Question 2 answer is: {answer_2}")
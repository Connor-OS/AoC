TEST = False
in_file = "./resources/day_3_test.txt" if TEST else "./resources/day_3.txt"

import re

def file_lines():

    # return open(in_file).read()

    with open(in_file) as file:
        for line in file:
            """Custom iteration logic goes here"""
            line = line.strip()
            yield line


def question_1():
    """Answer to the first question of the day"""
    answer = 0
    # data = *file_lines()
    # print(data)

    for line in file_lines():
        reg = re.findall(r"mul\(\d*,\d*\)", line)
        for i in reg:
            f,l = i.split(",")
            print(f[4:],"-",l[:-1])

            answer += int(f[4:]) * int(l[:-1])

    return answer


def question_2():
    """Answer to the second question of the day"""
    answer = 0
    do = True
    for line in file_lines():
        reg = re.findall(r"mul\(\d*,\d*\)|do\(\)|don't\(\)", line)
        for i in reg:
            print(i)
            if do == True and "mul" in i:
                f,l = i.split(",")
                print(f[4:],"-",l[:-1])

                answer += int(f[4:]) * int(l[:-1])
            elif i == "do()":
                do = True
            else:
                do = False

    return answer



if __name__ == '__main__':
    # answer_1 = question_1()
    # print(f"Question 1 answer is: {answer_1}")

    answer_2 = question_2()
    print(f"Question 2 answer is: {answer_2}")
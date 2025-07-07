TEST = False
in_file = "./resources/day_4_test.txt" if TEST else "./resources/day_4.txt"

from utils.input_handling import file_lines

def question_1():
    """Answer to the first question of the day"""
    answer = 0

    for i in range(248345, 746315):
       if criteria(i):
           answer += 1

    return answer

def criteria(number):
    l = list(str(number))

    if sorted(l) == l and len(set(l)) != len(l):
        return True



def criteria_2(number):
    l = list(str(number))

    if sorted(l) == l:
        run_len = 0
        current  = l[0]
        for i in l:
            if i == current:
                run_len += 1
            elif run_len == 2:
                return True
            else:
                current = i
                run_len = 1
        if run_len == 2:
            return True


def question_2():
    """Answer to the second question of the day"""
    answer = 0

    for i in range(248345, 746315):
        if criteria_2(i):
            answer += 1

    return answer



if __name__ == '__main__':
    answer_1 = question_1()
    print(f"Question 1 answer is: {answer_1}")

    answer_2 = question_2()
    print(f"Question 2 answer is: {answer_2}")

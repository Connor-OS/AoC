TEST = False
in_file = "./resources/day_25_test.txt" if TEST else "./resources/day_25.txt"

def file_lines():
    locks = []
    keys = []
    with open(in_file) as file:
        for block in file.read().split("\n\n"):
            """Custom iteration logic goes here"""
            counter = count_key_lock(block)
            if block[0] == "#":
                keys.append(counter)
            else:
                locks.append(counter)
        return keys, locks


def count_key_lock(lines):
    counter = [-1]*5

    for y, row in enumerate(lines.splitlines()):
        for x, char in enumerate(row.strip("\n")):
            if char == "#":
                counter[x] += 1

    return counter


def question_1():
    """Answer to the first question of the day"""
    answer = 0
    keys, locks = file_lines()
    print(keys, locks)

    for lock in locks:
        for key in keys:
            answer += test_key(lock, key)




    return answer

def test_key(lock, key):
    for pin in range(5):
        if lock[pin] + key[pin] > 5:
            return 0

    return 1


def question_2():
    """Answer to the second question of the day"""
    answer = 0

    return answer


if __name__ == '__main__':
    answer_1 = question_1()
    print(f"Question 1 answer is: {answer_1}")

    # answer_2 = question_2()
    # print(f"Question 2 answer is: {answer_2}")
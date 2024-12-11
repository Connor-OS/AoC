TEST = False
in_file = "./resources/day_9_test.txt" if TEST else "./resources/day_9.txt"


def file_lines():
    with open(in_file) as file:
        return file.read()


def question_1():
    """Answer to the first question of the day"""
    answer = 0
    files = [int(f) for f in file_lines()[::2]]
    gaps = [int(g) for g in file_lines()[1::2]]
    file_que = [[i] * f for i, f in enumerate(files)]
    file_que = [f for file in file_que for f in file]

    files.reverse()
    gaps.reverse()

    answer = process(files, gaps, file_que)
    return answer


def process(files, gaps, file_que):
    # two pointers from each end
    answer = 0
    i, j = 0, len(file_que) - 1

    count = 0
    while True:
        file = files.pop()
        for f in range(file):
            answer += count * file_que[i]
            i += 1
            count += 1
            if i > j: return answer
        gap = gaps.pop()
        for g in range(gap):
            answer += count * file_que[j]
            j -= 1
            count += 1
            if i > j: return answer


def question_2():
    """Answer to the second question of the day"""
    answer = 0

    files = [int(f) for f in file_lines()[::2]]
    gaps = [int(g) for g in file_lines()[1::2]]

    file_objects, gap_objects = construct_objects(files, gaps)
    file_objects.reverse()

    moved_files = []
    for file in file_objects:
        moved_files.append(try_move(file, gap_objects))

    for file_id, start, length in moved_files:
        for i in range(length):
            answer += file_id * (start + i)

    return answer


def construct_objects(files, gaps):
    # file: (file_id, start, length)
    # gap: (start, end)
    file_id, start = 0, 0
    file_objects, gap_objects = [], []
    for f, g in zip(files, gaps + [1]):
        file_objects.append((file_id, start, f))
        start += f
        gap_objects.append((start, start + g))
        start += g
        file_id += 1

    return file_objects, gap_objects


def try_move(file, gaps):
    file_id, file_start, length = file
    for i, gap in enumerate(gaps):
        start, end = gap
        if start < file_start and start + length <= end:
            file = (file_id, start, length)
            # modifying gap in place here is quite risky but works :)
            gaps[i] = (start + length, end)
            return file
    return file


if __name__ == '__main__':
    answer_1 = question_1()
    print(f"Question 1 answer is: {answer_1}")

    answer_2 = question_2()
    print(f"Question 2 answer is: {answer_2}")

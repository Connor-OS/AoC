TEST = False
in_file = "./resources/day_11_test.txt" if TEST else "./resources/day_11.txt"

from functools import lru_cache
from utils.input_handling import file_lines

severs = {}
for line in file_lines(in_file):
    line = line.split()
    key, values = line[0][:-1], line[1:]
    severs[key] = values

def question_1():
    """Answer to the first question of the day"""
    return _find_paths("you", "out")

def _find_paths(start, end):
    """Find all paths between start and end"""
    answer = 0
    front = [start]
    while front:
        pos = front.pop(0)

        if pos == end:
            answer += 1
            continue

        front.extend(severs[pos])

    return answer

@lru_cache
def find_paths(start, end):
    """Find all paths between start and end"""
    if start == end:
        return 1

    return sum([find_paths(pos, end) for pos in severs[start]])



def question_2():
    """Answer to the second question of the day"""
    answer = 0

    svr_fft = find_paths("svr", "fft")
    svr_dac = find_paths("svr", "dac")

    fft_dac = find_paths("fft", "dac")
    dac_fft = find_paths("dac", "fft")

    fft_out = find_paths("fft", "out")
    dac_out = find_paths("dac", "out")

    answer += svr_fft * fft_dac * dac_out
    answer += svr_dac * dac_fft * fft_out

    return answer


if __name__ == '__main__':
    answer_1 = question_1()
    print(f"Question 1 answer is: {answer_1}")

    answer_2 = question_2()
    print(f"Question 2 answer is: {answer_2}")

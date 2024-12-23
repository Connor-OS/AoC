TEST = True
in_file = "./resources/day_21_test.txt" if TEST else "./resources/day_21.txt"

numeric_key_pad = {"7": (0, 0), "8": (1, 0), "9": (2, 0),
                   "4": (0, 1), "5": (1, 1), "6": (2, 1),
                   "1": (0, 2), "2": (1, 2), "3": (2, 2),
                                "0": (1, 3), "A": (2, 3)}

directional_key_pad = {"^": (1, 0), "A": (2, 0),
          "<": (0, 1), "v": (1, 1), ">": (2, 1)}

DIRS = {">": (1, 0), "<": (-1, 0), "v": (0, 1), "^": (0, -1)}


def file_lines():
    with open(in_file) as file:
        for line in file:
            """Custom iteration logic goes here"""
            line = line.strip()
            yield line


def question_1():
    """Answer to the first question of the day"""
    answer = 0

    for sequence in file_lines():
        code = int(sequence[:-1])
        sequence = desequence(sequence)
        answer += len(sequence) * code

    return answer


def desequence(sequence):
    print(f"{sequence} - {len(sequence)}")
    sequence = translate(sequence, numeric_key_pad, (0, 3))
    print(f"{sequence} - {len(sequence)}")
    sequence = translate(sequence, directional_key_pad)
    print(f"{sequence} - {len(sequence)}")
    sequence = translate(sequence, directional_key_pad)
    print(f"{sequence} - {len(sequence)}")
    return sequence


def translate(sequence, key_pad, bad_square=(0, 0)):
    bad_x, bad_y = bad_square

    pointer = key_pad["A"]
    inputs = ""
    for button in sequence:
        target = key_pad[button]
        p_x, p_y = pointer
        d_x, d_y = manhatan_dist(pointer, target)

        bad = p_x + d_x == bad_x and p_y == bad_y

        moves = ""
        moves += abs(d_x) * "<" if d_x < 0 else ""
        moves += d_y * "v" if d_y > 0 else abs(d_y) * "^"
        moves += d_x * ">" if d_x > 0 else ""

        # for i, move in enumerate(moves):
        #     if move == "A": continue
        #     s_x, s_y = DIRS[move]
        #     step = (p_x + s_x, p_y + s_y)
        #     if step == bad_square:
        #         moves = moves[:i] + moves[i+1:] + moves[i]
        #         break
        #     p_x, p_y = step

        moves += "A"
        inputs += moves
        pointer = target

    return inputs


def manhatan_dist(pointer, target):
    p_x, p_y = pointer
    t_x, t_y = target

    return t_x - p_x, t_y - p_y


def question_2():
    """Answer to the second question of the day"""
    answer = 0

    return answer


if __name__ == '__main__':


    answer_1 = question_1()
    print(f"Question 1 answer is: {answer_1}")

    # answer_2 = question_2()
    # print(f"Question 2 answer is: {answer_2}")

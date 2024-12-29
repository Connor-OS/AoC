# Worst code know to man


TEST = False
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
    # print(f"{sequence} - {len(sequence)}")
    sequence = translate(sequence, numeric_key_pad, (0, 3))
    # print(f"{sequence} - {len(sequence)}")
    sequence = translate(sequence, directional_key_pad)
    # print(f"{sequence} - {len(sequence)}")
    sequence = translate(sequence, directional_key_pad)
    # print(f"{sequence} - {len(sequence)}")
    return sequence


def translate(sequence, key_pad, bad_square=(0, 0)):
    pointer = key_pad["A"]
    inputs = ""
    for button in sequence:
        target = key_pad[button]
        p_x, p_y = pointer
        d_x, d_y = manhatan_dist(pointer, target)

        moves = ""
        moves += abs(d_x) * "<" if d_x < 0 else ""
        moves += d_y * "v" if d_y > 0 else abs(d_y) * "^"
        moves += d_x * ">" if d_x > 0 else ""

        moves = moves.split("A")
        for i, move in enumerate(moves):
            for j, s in enumerate(move):
                new_move = None
                s_x, s_y = DIRS[s]
                step = (p_x + s_x, p_y + s_y)
                if step == bad_square:
                    new_move = swap(move)
                p_x, p_y = step
                if new_move:
                    moves[i] = new_move

        moves = "A".join(moves)

        moves += "A"
        inputs += moves
        pointer = target

    return inputs

def desequence_2(sequence):

    sequence = translate_sequence(sequence, "numeric", (0, 3))

    for i in range(25):
        sequence = translate_sequence(sequence)

    return sequence


def translate_sequence(sequence, key_pad=None, bad_square=(0, 0)):
    sequence_dict = {}
    for move in sequence:
        start, end = move
        move_sequence = translate_move(start, end, key_pad, bad_square)
        if move_sequence:
            move_sequence = [("A", move_sequence[0][0])] + move_sequence
        else:
            move_sequence = [("A", "A")]


        for s in move_sequence:
            sequence_dict.setdefault(s, 0)
            sequence_dict[s] += 1*sequence.get(move)

    return sequence_dict


def translate_move(start, end, key_pad=None, bad_square=(0, 0)):
    if key_pad == "numeric":
        key_pad = numeric_key_pad
    else: key_pad = directional_key_pad
    pointer = key_pad[start]

    target = key_pad[end]
    d_x, d_y = manhatan_dist(pointer, target)

    moves = ""
    moves += abs(d_x) * "<" if d_x < 0 else ""
    moves += d_y * "v" if d_y > 0 else abs(d_y) * "^"
    moves += d_x * ">" if d_x > 0 else ""

    p_x, p_y = pointer
    for j, s in enumerate(moves):
        new_move = None
        s_x, s_y = DIRS[s]
        step = (p_x + s_x, p_y + s_y)
        if step == bad_square:
            new_move = swap(moves)
        p_x, p_y = step
        if new_move:
            moves = new_move

    moves += "A"

    return [(moves[i], moves[i + 1]) for i, _ in enumerate(moves[:-1])]


def swap(move):
    # why on earth does this actually work??
    char_1 = move[0]
    char_2 = move[-1]
    move = move.replace(char_1, "*")
    move = move.replace(char_2, char_1)
    move = move.replace("*", char_2)
    return move


def manhatan_dist(pointer, target):
    p_x, p_y = pointer
    t_x, t_y = target

    return t_x - p_x, t_y - p_y


def question_2():
    """Answer to the second question of the day"""
    answer = 0

    for sequence in file_lines():
        code = int(sequence[:-1])

        sequence = [('A', sequence[0])] + [(sequence[i], sequence[i + 1]) for i, _ in enumerate(sequence[:-1])]

        sequence_dict = {}
        for s in sequence:
            sequence_dict.setdefault(s, 0)
            sequence_dict[s] += 1

        sequence = desequence_2(sequence_dict)

        sequence_length = 0
        for repeat in sequence.values():
            sequence_length += repeat

        answer += sequence_length * code

    return answer


def experiment():
    sequence = input("input sequence: ")
    print(f"{sequence} - {len(sequence)}")
    sequence = translate(sequence, numeric_key_pad, (0, 3))
    print(f"{sequence} - {len(sequence)}")
    sequence = translate(sequence, directional_key_pad)
    print(f"{sequence} - {len(sequence)}")
    sequence = translate(sequence, directional_key_pad)
    print(f"{sequence} - {len(sequence)}")


if __name__ == '__main__':
    # while True:
    #     experiment()
    #
    answer_1 = question_1()
    print(f"Question 1 answer is: {answer_1}")

    answer_2 = question_2()
    print(f"Question 2 answer is: {answer_2}")

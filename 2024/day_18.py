TEST = False
in_file = "./resources/day_18_test.txt" if TEST else "./resources/day_18.txt"
bytes_num = 12 if TEST else 1024
wall_size = 8 if TEST else 72

DIRS = ((1, 0), (-1, 0), (0, 1), (0, -1))


def file_lines(bytes_num):

    grid = {}
    for x in range(wall_size+1):
        grid[(x,0)] = "#"
        grid[(x,wall_size)] = "#"

    for y in range(wall_size+1):
        grid[(0,y)] = "#"
        grid[(wall_size, y)] = "#"

    with open(in_file) as file:
        for i, line in enumerate(file):
            if i == bytes_num:
                break
            x,y = line.split(",")
            grid[(int(x)+1, int(y)+1)] = "#"
    return grid


def question_1(bytes=bytes_num):
    """Answer to the first question of the day"""
    grid = file_lines(bytes)
    start = (1, 1)
    end = (wall_size-1, wall_size-1)
    visited = []

    front = [(start, 0)]

    while front:
        best = best_element(front)
        point, score = front.pop(best)

        if point == end:
            return score

        visited.append(point)

        p_x, p_y = point
        for d_x, d_y in DIRS:
            step = (p_x + d_x, p_y + d_y)
            if step not in grid and step not in visited:
                front.append((step, score+1))

    return None


def best_element(front):
    closeness = float("inf")
    best_index = 0
    t_x, t_y = wall_size-1, wall_size-1
    for i, elem in enumerate(front):
        elem, score = elem
        e_x, e_y = elem
        if score + abs(t_x - e_x) + abs(t_y - e_y) <= closeness:
            closeness = score + abs(t_x - e_x) + abs(t_y - e_y)
            best_index = i
    return best_index


def question_2():
    """Answer to the second question of the day"""
    bytes_list = [line for line in open(in_file)]
    max_bytes = len(bytes_list)

    while not question_1(max_bytes):
        max_bytes -= 1

    return bytes_list[max_bytes]


if __name__ == '__main__':
    answer_1 = question_1()
    print(f"Question 1 answer is: {answer_1}")

    answer_2 = question_2()
    print(f"Question 2 answer is: {answer_2}")
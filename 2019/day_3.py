TEST = False
in_file = "./resources/day_3_test.txt" if TEST else "./resources/day_3.txt"

from utils.input_handling import file_lines

def question_1():
    """Answer to the first question of the day"""
    line_1, line_2 = file_lines(in_file)

    line_1 = line_1.split(",")
    line_2 = line_2.split(",")

    segments_1 = line_segments(line_1)
    segments_2 = line_segments(line_2)

    intersctions = []
    for horiz_seg in segments_1[0]:
        for vert_seg in segments_2[1]:
            if inter := intersesct_lines(horiz_seg, vert_seg):
                intersctions.append(inter)

    for horiz_seg in segments_2[0]:
        for vert_seg in segments_1[1]:
            if inter := intersesct_lines(horiz_seg, vert_seg):
                intersctions.append(inter)

    return min([a+b for a, b in intersctions])


def intersesct_lines(line_1, line_2):
    p, range_1, _, _ = line_1
    q, range_2, _, _ = line_2

    if range_1[0] < q < range_1[1] and range_2[0] < p < range_2[1]:
        return p,q

    return None

def intersesct_lines_2(line_1, line_2):
    p, range_1, d_1, dir_1 = line_1
    q, range_2, d_2, dir_2 = line_2

    extra = 0
    if dir_1 in ['U', 'R']:
        extra += p - range_1[0]
    else:
        extra += range_1[1] - p

    if dir_2 in ['U', 'R']:
        extra += q - range_2[0]
    else:
        extra += range_2[1] - q

    if range_1[0] < q < range_1[1] and range_2[0] < p < range_2[1] and extra > 0:
        print(d_1 + d_2)
        print(extra)

        return d_1 + d_2 + extra

    return None

def line_segments(line):
    point = (0,0)
    horizontal = []
    vertical = []
    dist = 0

    for move in line:
        direction = move[0]
        distance = int(move[1:])
        x, y = point
        if direction == 'U':
            next = (x, y + distance)
            vertical.append((x, (y,y+distance), dist, direction))
        if direction == 'D':
            next = (x, y - distance)
            vertical.append((x, (y - distance, y), dist, direction))
        if direction == 'R':
            next = (x + distance, y)
            horizontal.append((y, (x, x + distance), dist, direction))
        if direction == 'L':
            next = (x - distance, y)
            horizontal.append((y, (x - distance, x), dist, direction))
        point = next
        dist += distance

    return horizontal, vertical


def question_2():
    """Answer to the second question of the day"""
    line_1, line_2 = file_lines(in_file)

    line_1 = line_1.split(",")
    line_2 = line_2.split(",")

    segments_1 = line_segments(line_1)
    segments_2 = line_segments(line_2)

    intersctions = []
    for horiz_seg in segments_1[0]:
        for vert_seg in segments_2[1]:
            if inter := intersesct_lines_2(horiz_seg, vert_seg):
                intersctions.append(inter)

    for horiz_seg in segments_2[0]:
        for vert_seg in segments_1[1]:
            if inter := intersesct_lines_2(horiz_seg, vert_seg):
                intersctions.append(inter)

    print(intersctions)

    return min(intersctions)

if __name__ == '__main__':
    answer_1 = question_1()
    print(f"Question 1 answer is: {answer_1}")

    answer_2 = question_2()
    print(f"Question 2 answer is: {answer_2}")

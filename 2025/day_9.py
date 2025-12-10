TEST = False
in_file = "./resources/day_9_test.txt" if TEST else "./resources/day_9.txt"

from utils.input_handling import file_lines, render_grid

def get_tiles():
    tiles = []
    for line in file_lines(in_file):
        x,y = line.split(",")
        tiles.append((int(x), int(y)))
    return tiles

def rect_area(t1, t2):
    t1x, t1y = t1
    t2x, t2y = t2
    return (abs(t1x - t2x)+1) * (abs(t1y - t2y)+1)

def question_1():
    """Answer to the first question of the day"""
    answer = 0
    tiles = get_tiles()

    for i, tile1 in enumerate(tiles):
        for tile2 in tiles[i+1:]:
            rect = rect_area(tile1, tile2)
            if rect > answer:
                answer = rect

    return answer


def intersection(p1, p2, p3, p4, r1, r2):
        if r1 in [p1, p2] and r1 in [p3, p4] or r2 in [p1, p2] and r2 in [p3, p4]:
            return None
        x1, y1 = p1
        x2, y2 = p2
        x3, y3 = p3
        x4, y4 = p4
        denom = (y4 - y3) * (x2 - x1) - (x4 - x3) * (y2 - y1)
        if denom == 0:  # parallel
            return None
        ua = ((x4 - x3) * (y1 - y3) - (y4 - y3) * (x1 - x3)) / denom
        if ua < 0 or ua > 1:  # out of range
            return None
        ub = ((x2 - x1) * (y1 - y3) - (y2 - y1) * (x1 - x3)) / denom
        if ub < 0 or ub > 1:  # out of range
            return None

        if ua == 0 or ua == 1 or ub == 0 or ub == 1:
            return None
        return True

def check_intersect(rect, lines):

    r1, r2 = rect
    r3 = (r1[0], r2[1])
    r4 = (r2[0], r1[1])
    rect = [(r1, r3), (r3, r2), (r2, r4), (r4, r1)]

    for side in rect:
        for line in lines:

            if intersection(side[0], side[1], line[0], line[1], r1, r2):
                return True
    return False

def check_inside(laser, lines):
    crosses = 0
    for line in lines:
        if intersection(laser[0], laser[1], line[0], line[1]):
            crosses += 1

    return False if crosses%2==0 else True

def point_inside_rect(x1,x2,y1,y2,px,py):
    return x1 < px < x2 and y1 < py < y2

def sign(a, b):
    diff = b - a
    return 1 if diff > 0 else -1 if diff < 0 else 0

def check_all_points_outside(rect: (tuple, tuple), points):
    x1, y1 = rect[0]
    x2, y2 = rect[1]

    if x1 > x2:
        _ = x1
        x1 = x2
        x2 = _

    if y1 > y2:
        _ = y1
        y1 = y2
        y2 = _

    for i, point in enumerate(points):
        px, py = point
        if px in [x1, x2] or py in [y1, y2]:
            sx, sy = points[(i+1) % len(points)]
            dx = px + sign(px, sx)
            dy = py + sign(py, sy)
            if point_inside_rect(x1, x2, y1, y2, dx, dy):
                return False

            sx, sy = points[(i-1) % len(points)]
            dx = px + sign(px, sx)
            dy = py + sign(py, sy)
            if point_inside_rect(x1, x2, y1, y2, dx, dy):
                return False

        if point_inside_rect(x1,x2,y1,y2,px,py):
            return False
    return True


def question_2():
    """Answer to the second question of the day"""
    answer = 0
    tiles = get_tiles()

    lines = [(t,tiles[(i+1) % len(tiles)]) for i,t in enumerate(tiles)]

    for i, tile1 in enumerate(tiles):
        for tile2 in tiles[i+1:]:

            if not check_all_points_outside((tile1, tile2),tiles):
                continue

            if check_intersect((tile1,tile2),lines):
               continue

            rect = rect_area(tile1, tile2)

            if rect > answer:
                answer = rect

    return answer


if __name__ == '__main__':
    answer_1 = question_1()
    print(f"Question 1 answer is: {answer_1}")

    answer_2 = question_2() # 2334903301
    print(f"Question 2 answer is: {answer_2}")

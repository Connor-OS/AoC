TEST = False
in_file = "./resources/day_12_test.txt" if TEST else "./resources/day_12.txt"
from utils.input_handling import read_grid, render_grid

grid = read_grid(in_file)

DIRS = ((1, 0), (-1, 0), (0, 1), (0, -1))


def question_1():
    """Answer to the first question of the day"""
    answer_1, answer_2 = 0,0
    # render_grid(grid)

    global_visited = [point for point in grid.items()]

    while global_visited:
        point, value = global_visited.pop()
        front = [point]
        visited = []
        region_perim = 0
        region_area = 0
        sides = []
        while front:

            point = front.pop()
            if point in visited: continue
            region_area += 1

            visited.append(point)

            p_x, p_y = point
            for d_x, d_y in DIRS:
                step = (p_x + d_x, p_y + d_y)

                if step not in grid or grid.get(step) != value:
                    region_perim += 1

                    if (point, (d_x, d_y)) not in sides:
                        sides.append((point, (d_x, d_y)))

                if grid.get(step) == value and step not in visited:
                    front.append(step)

            if (point, value) in global_visited:
                global_visited.remove((point, value))

        num_sides = check_sides(sides)
        # print(f"region {value} area: {region_area} perim: {num_sides}")
        answer_1 += region_area * region_perim
        answer_2 += region_area * num_sides

    return answer_1, answer_2


def check_sides(sides):
    side_count = 0
    while sides:
        # print(sides)
        side_count += 1
        side, perp_dir = sides.pop()
        s_x, s_y = side
        d_x, d_y = rotate_clockwise(*perp_dir)
        step = ((s_x + d_x, s_y + d_y), perp_dir)
        while step in sides:
            sides.remove(step)
            s_x += d_x
            s_y += d_y
            step = ((s_x + d_x, s_y + d_y), perp_dir)

        s_x, s_y = side
        d_x, d_y = rotate_anti_clockwise(*perp_dir)
        step = ((s_x + d_x, s_y + d_y), perp_dir)
        while step in sides:
            sides.remove(step)
            s_x += d_x
            s_y += d_y
            step = ((s_x + d_x, s_y + d_y), perp_dir)
    return side_count


def rotate_clockwise(d_x, d_y):
    return -d_y, d_x


def rotate_anti_clockwise(d_x, d_y):
    return d_y, -d_x


if __name__ == '__main__':
    answer_1, answer_2 = question_1()
    print(f"Question 1 answer is: {answer_1}")
    print(f"Question 2 answer is: {answer_2}")

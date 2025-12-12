TEST = False
in_file = "./resources/day_7_test.txt" if TEST else "./resources/day_7.txt"

from utils.input_handling import read_grid, render_grid

grid = read_grid(in_file)
splits = 0


def find_start():
    for start in grid:
        if grid[start] == "S":
            return start
    return None

def shoot_beam(pos):
    beams = 0
    render_grid(grid)

    px, py = pos
    new_pos = (px, py+1)
    if new_pos not in grid:
        return 1

    if grid[new_pos] == "|":
        return 0

    if grid[new_pos] == ".":
        grid[new_pos] = "|"
        beams += shoot_beam(new_pos)

    if grid[new_pos] == "^":
        global splits
        splits += 1
        beams += shoot_beam((px+1, py+1))
        beams += shoot_beam((px - 1, py + 1))

    return beams

def question_1():
    """Answer to the first question of the day"""

    start = find_start()

    shoot_beam(start)
    return splits

def shoot_beams(front):

    # render_grid(grid)
    new_front = []
    for pos in front:

        px, py = pos
        new_pos = (px, py+1)
        if new_pos not in grid:
            # print(front)
            # print([grid[f] for f in front])
            print(sum([grid[f] for f in front]))
            return

        if grid[new_pos] == 0:
            new_front.append(new_pos)
            grid[new_pos] += grid[pos]

        elif grid[new_pos] > 0:
            grid[new_pos] += grid[pos]
        else:

            new_pos = (px+1, py+1)
            grid[new_pos] += grid[pos]
            if new_pos not in new_front:
                new_front.append(new_pos)

            new_pos = (px - 1, py + 1)
            grid[new_pos] += grid[pos]
            if new_pos not in new_front:
                new_front.append(new_pos)

    return new_front



def question_2():
    """Answer to the second question of the day"""
    answer = 0

    start = find_start()
    grid[start] = 1

    for key in grid:
        if grid[key] == ".":
            grid[key] = 0
        if grid[key] == "^":
            grid[key] = -1

    front = [start]
    while front := shoot_beams(front):
        print(front)
        # print(sum(([grid[f] for f in front])))
    # print(len(front))

    return splits + 1


if __name__ == '__main__':
    answer_1 = question_1()
    print(f"Question 1 answer is: {answer_1}")

    answer_2 = question_2()
    print(f"Question 2 answer is: {answer_2}")

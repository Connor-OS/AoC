TEST = False
in_file = "./resources/day_14_test.txt" if TEST else "./resources/day_14.txt"
import re
from matplotlib import pyplot as plt
import numpy as np

SPACE_DIMENSIONS = [11, 7] if TEST else [101, 103]

def file_lines():
    with open(in_file) as file:
        for line in file:
            """Custom iteration logic goes here"""
            line = line.strip()
            yield [int(i) for i in re.findall("-?\d+", line)]


def read_robots():

    robots = {}
    bot_num = 0
    for x,y,v_x, v_y in file_lines():
        robots[f"Bot_{bot_num}"] = ((x,y),(v_x,v_y))
        bot_num += 1
    return robots

def move_bots(robots, t):
    bots_at_time_t = {}
    for bot in robots:
        pos, vel = robots[bot]
        pos_x, pos_y = pos
        vel_x, vel_y = vel
        pos_x += vel_x*t
        pos_x = pos_x % SPACE_DIMENSIONS[0]
        pos_y += vel_y*t
        pos_y = pos_y % SPACE_DIMENSIONS[1]
        bots_at_time_t[bot] = ((pos_x, pos_y), vel)
    return bots_at_time_t

def render_bots(robots):
    bots = [pos for pos,vel in robots.values()]
    for i in range(SPACE_DIMENSIONS[1]):
        for j in range(SPACE_DIMENSIONS[0]):
            if (j,i) in bots:
                print("#",end="")
            else:
                print(" ",end="")
        print()

def render_bots_np(robots):
    bots = [pos for pos,vel in robots.values()]
    render = np.zeros(SPACE_DIMENSIONS)
    for i in range(SPACE_DIMENSIONS[1]):
        for j in range(SPACE_DIMENSIONS[0]):
            if (j,i) in bots:
                render[j,i] += 1

    plt.imshow(render)
    plt.show()


def question_1():
    """Answer to the first question of the day"""
    answer = 0

    robots = read_robots()
    render_bots(robots)

    robots = move_bots(robots, 100)

    render_bots(robots)

    quadrants = [0,0,0,0]
    bots = [pos for pos,vel in robots.values()]
    x_half = SPACE_DIMENSIONS[0]/2
    y_half = SPACE_DIMENSIONS[1]/2

    for pos_x, pos_y in bots:
        if pos_x < x_half-1 and pos_y < y_half-1:
            quadrants[0] += 1
        if pos_x < x_half-1 and pos_y > y_half:
            quadrants[1] += 1
        if pos_x > x_half and pos_y < y_half-1:
            quadrants[2] += 1
        if pos_x > x_half and pos_y > y_half:
            quadrants[3] += 1

    a,b,c,d = quadrants


    return a*b*c*d

def bot_density(robots):
    bots = [pos for pos,vel in robots.values()]

    density = 0
    for p_x, p_y in bots:
        dist = 0
        for o_x, o_y in bots:
            dist += ((p_x - o_x)**2 + (p_y - o_y)**2)**0.5
        density += 1/dist

    return density


def question_2():
    """Answer to the second question of the day"""

    # input cycles at: 10403 from investigation
    robots = read_robots()

    christmas_easter_egg =0

    max_density = 0
    for t in range(10403):
        robots = move_bots(robots, 1)
        density = bot_density(robots)
        if density > max_density:
            max_density = density
            christmas_easter_egg = t+1

    robots = read_robots()
    robots = move_bots(robots, 8280)
    render_bots_np(robots)

    return christmas_easter_egg





if __name__ == '__main__':
    # answer_1 = question_1()
    # print(f"Question 1 answer is: {answer_1}")

    answer_2 = question_2()
    print(f"Question 2 answer is: {answer_2}")
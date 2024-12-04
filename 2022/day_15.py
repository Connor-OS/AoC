TEST = False
in_file = "./resources/day_15_test.txt" if TEST else "./resources/day_15_input.txt"


def file_lines():
    with open(in_file) as file:
        for line in file:
            """Custom iteration logic goes here"""
            line = line.replace("Sensor at x=", "")
            line = line.replace(" y=", "")
            line = line.replace(": closest beacon is at x=", ",")
            line = [int(i) for i in line.split(",")]
            yield line


def question_1():
    """Answer to the first question of the day"""
    answer = 0
    line = 2000000

    sensors = [(l[0], l[1]) for l in file_lines()]
    sensor_range = [abs(l[0] - l[2]) + abs(l[1] - l[3]) for l in file_lines()]

    spreads = []
    for sensor, spread in zip(sensors, sensor_range):
        dy = abs(sensor[1] - line)

        # print(dy, spread)
        if dy > spread:
            continue


        spreads.append((sensor[0] - abs(dy - spread), sensor[0] + abs(dy - spread)))

    spreads.sort()

    upto = spreads[0][0]
    for spread in spreads:
        if spread[1] < upto: continue

        if spread[0] <= upto:
            answer += spread[1] - upto
        else:

            answer += spread[1] - (spread[0]-1)
        upto = spread[1]

    return answer

def question_2_handler():
    sensors = [(l[0], l[1]) for l in file_lines()]
    sensor_range = [abs(l[0] - l[2]) + abs(l[1] - l[3]) for l in file_lines()]

    for i in range(4000000):
        if i% 1000 == 0: print(i)
        if answer := question_2(sensors, sensor_range, i):
            return answer


def question_2(sensors, sensor_range, line):
    """Answer to the second question of the day"""

    spreads = []
    for sensor, spread in zip(sensors, sensor_range):
        dy = abs(sensor[1] - line)

        if dy > spread:
            continue

        spreads.append((sensor[0] - abs(dy - spread), sensor[0] + abs(dy - spread)))

    spreads.sort()

    upto = 0
    for spread in spreads:
        if spread[1] < upto: continue
        if upto+1 < spread[0]:
            return upto + 1

        upto = spread[1]
    return




if __name__ == '__main__':
    # answer_1 = question_1()
    # print(f"Question 1 answer is: {answer_1}")

    answer_2 = question_2_handler()
    print(f"Question 2 answer is: {answer_2}")

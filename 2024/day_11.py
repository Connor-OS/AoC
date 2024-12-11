TEST = False
in_file = "./resources/day_11_test.txt" if TEST else "./resources/day_11.txt"


def file_lines():
    with open(in_file) as file:
        return file.read().split()


def question_1():
    """Answer to the first question of the day"""

    stones = file_lines()
    for t in range(25):
        new_stones = []
        for stone in stones:
            if stone == "0":
                new_stones.append("1")
            elif len(stone)%2 == 0:
                new_stones.append(stone[:int(len(stone)/2)])
                new_stones.append(str(int(stone[int(len(stone)/2):])))
            else:
                new_stones.append(str(int(stone) * 2024))

        stones = new_stones
        # print(stones)
        # print(len(stones))

    return len(stones)


def question_2():
    """Answer to the second question of the day"""
    answer = None

    stones = {}
    input = file_lines()
    for stone in input:
        if stones.get(stone):
            stones[stone] += 1
        else:
            stones[stone] = 1

    for t in range(75):
        new_stones = {}
        for stone in stones:

            stone_number = stones[stone]

            if stone == "0":
                new_stone = "1"

                if new_stones.get(new_stone):
                    new_stones[new_stone] += stone_number
                else:
                    new_stones[new_stone] = stone_number

            elif len(stone)%2 == 0:
                stone_a = stone[:int(len(stone)/2)]
                stone_b = str(int(stone[int(len(stone)/2):]))

                if new_stones.get(stone_a):
                    new_stones[stone_a] += stone_number
                else:
                    new_stones[stone_a] = stone_number

                # if stone_b == "0": continue
                if new_stones.get(stone_b):
                    new_stones[stone_b] += stone_number
                else:
                    new_stones[stone_b] = stone_number

            else:

                new_stone = (str(int(stone) * 2024))

                if new_stones.get(new_stone):
                    new_stones[new_stone] += stone_number
                else:
                    new_stones[new_stone] = stone_number
        stones = new_stones

    answer = 0
    for stone in stones:
        answer += stones[stone]

    return answer

if __name__ == '__main__':
    answer_1 = question_1()
    print(f"Question 1 answer is: {answer_1}")

    answer_2 = question_2()
    print(f"Question 2 answer is: {answer_2}") #221291560078593
TEST = False
in_file = "./resources/day_22_test.txt" if TEST else "./resources/day_22.txt"
from collections import deque
from time import time

def file_lines():
    with open(in_file) as file:
        for line in file:
            """Custom iteration logic goes here"""
            line = line.strip()
            yield int(line)


def question_1():
    """Answer to the first question of the day"""
    answer = 0
    for secret_number in file_lines():
        for i in range(2000):
            secret_number = mutate(secret_number)

        answer += secret_number

    return answer


def mutate(secret_number):
    secret_number = mix(secret_number, 64 * secret_number)
    secret_number = prune(secret_number)

    secret_number = mix(secret_number, int(secret_number / 32))
    secret_number = prune(secret_number)

    secret_number = mix(secret_number, 2048 * secret_number)
    return prune(secret_number)


def mix(secret_number, mixin):
    return secret_number ^ mixin


def prune(secret_number):
    return secret_number % 16777216


def question_2():
    """Answer to the second question of the day"""
    answer = 0
    buyers = []

    for buyer, secret_number in enumerate(file_lines()):
        buyers.append([secret_number%10])
        for i in range(2000):
            secret_number = mutate(secret_number)
            buyers[buyer].append(secret_number%10)

    num_buyers = len(buyers)

    for buyer_seq, sequence in sequences(buyers):

        if (num_buyers-buyer_seq) * 9 < answer:
            break

        bananas = compute_buyers(buyers, sequence, answer)

        if bananas > answer:
            answer = bananas
            print(f"{answer}: {sequence}")

    return answer

def compute_buyers(buyers, sequence, to_beat):
    bananas = 0
    num_buyers = len(buyers)
    for i, buyer in enumerate(buyers):
        bananas += compute_bananas(buyer, sequence)
        if bananas + (num_buyers-i) * 9 < to_beat:
            return 0

    return bananas


def compute_bananas(buyer, sequence):

    changes = deque()
    for i, price in enumerate(buyer[1:]):
        if len(changes) == 4:
            changes.popleft()
        changes.append(price - buyer[i])
        if tuple(changes) == sequence:
            return price
    return 0


def sequences(buyers):
    seen = []
    for j, buyer in enumerate(buyers):
        queue = deque()
        for i, price in enumerate(buyer[1:]):
            if len(queue) == 4:
                queue.popleft()
            queue.append(price - buyer[i])
            changes = tuple(queue)

            if len(changes) == 4 and changes not in seen:
                yield j, changes
            seen.append(changes)


if __name__ == '__main__':
    answer_1 = question_1()
    print(f"Question 1 answer is: {answer_1}")

    answer_2 = question_2()
    print(f"Question 2 answer is: {answer_2}")

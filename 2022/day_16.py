import time
from itertools import combinations

file_path = "./resources/day_16.txt"

from copy import deepcopy as copy
from functools import cache

PATHS = {}


def construct_network() -> dict:
    """
    Read input file and construct a pipe object for each line
    :return: network of connected nodes
    """
    network = {}
    with open(file_path) as file:
        for line in file:
            line = line.split()
            label = line[1]
            reward = int(line[4].strip(";").split("=")[1])
            neighbours = [i.strip(",") for i in line[9:]]
            # distances = [1] * len(neighbours)
            new_pipe = {"reward": reward, "neighbours": neighbours}
            network[label] = new_pipe
    return network


def simplify_network(network: dict) -> dict:
    """
    Use a breadth first search tactic to find the shortest
    routes between weighted nodes and drop zero weight nodes

    :param network:
    :return: simplified network of connected nodes
    """
    simplified_network = {}
    for node_id in network:

        node = network[node_id]
        if node["reward"] == 0 and node_id != "AA":
            continue
        neighbours = []
        distances = []
        visited = [node_id]
        moves = node["neighbours"]
        distance = 0

        while len(moves) > 0:
            next_moves = []
            distance += 1
            for move in moves:
                new_node = network[move]
                visited.append(move)
                if new_node["reward"] > 0:
                    neighbours.append(move)
                    distances.append(distance)
                next_moves.extend(new_node["neighbours"])
            next_moves = list(set(_ for _ in next_moves if _ not in visited))
            moves = next_moves
        simplified_network[node_id] = {"reward": node["reward"], "neighbours": neighbours, "distances": distances}
    return simplified_network


network = construct_network()

network = simplify_network(network)


def best_path(visited: tuple, cursor: str, t: int):
    """
    Function to recursively explore all potential paths in the network
    :param visited:
    :param cursor:
    :param t:
    :return: maximum scoring path
    """
    global network

    visited = list(visited)

    neighbours = network[cursor]["neighbours"]
    distances = network[cursor]["distances"]

    visited.append(cursor)

    score = network[cursor]["reward"] * t
    t -= 1

    if t <= 0 or set(network.keys()) == set(visited):
        return score

    # iterate through neighbours calling function on reduced network
    score += max([best_path(tuple(visited), n, t-d) for n, d in zip(neighbours, distances) if n not in visited] + [0])

    return score


def question_1():
    """Answer to the first question of the day"""
    return best_path((), "AA", 30)


def question_2():
    """Answer to the second question of the day"""
    best = 0

    for comb in combinations(set(network.keys()), int(len(network.keys())/2)):
        path = best_path(tuple(comb), "AA", 26)
        alt = set(network.keys()) - set(comb)
        path += best_path(tuple(alt), "AA", 26)
        if path > best:
            best = path
    return best

if __name__ == '__main__':

    tic = time.time()
    answer_1 = question_1()
    print(f"Question 1 answer is: {answer_1}") # correct answer is 1638
    toc = time.time()

    print(f"time: {toc-tic}s")

    answer_2 = question_2()
    print(f"Question 2 answer is: {answer_2}") # 1732
    toc = time.time()

    print(f"{toc-tic}s")



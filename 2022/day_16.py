file_path = "./resources/day_16.txt"

from copy import deepcopy as copy
# from functools import cache
#
# @cache # dist is not hashable
def best_path(network: dict, cursor: str, t: int, dist: int):
    '''
    Function to recursively explore all potential paths in the network
    :param network:
    :param cursor:
    :param t:
    :param dist:
    :return: maximum scoring path
    '''
    if t <= 0 or len(network) == 0:
        return 0

    # decrement time
    t -= dist

    # calculate score
    score = network[cursor]["reward"] * t

    t -= 1

    neighbours = network[cursor]["neighbours"]
    distances = network[cursor]["distances"]

    # Remove cursor from network
    updated_network = remove_node(copy(network), cursor)

    # iterate through neighbours calling function on reduced network
    score += max([best_path(updated_network, n, t, d) for n, d in zip(neighbours, distances)] + [0])

    len(network)
    return score


def remove_node(network: dict, cursor: str) -> dict:
    network.pop(cursor)
    for node in network:
        try:
            (network[node]["neighbours"],
             network[node]["distances"]) = (
                zip(*[(n, d) for n, d in zip(
                    network[node]["neighbours"],
                    network[node]["distances"]) if n != cursor]))
        except:
            network[node]["neighbours"] = ()
            network[node]["distances"] = ()
    return network


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


if __name__ == '__main__':
    network = construct_network()

    network = simplify_network(network)

    high_score = best_path(network, "AA", 30, 0)
    print(high_score)

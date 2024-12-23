TEST = True
in_file = "./resources/day_23_test.txt" if TEST else "./resources/day_23.txt"
import graphviz
from copy import deepcopy as copy
from functools import cache

clusters = []
graph = {}
with open(in_file) as file:
    for line in file:
        """Custom iteration logic goes here"""
        line = line.strip()
        node_a, node_b = line.split("-")
        if node_a not in graph:
            graph[node_a] = [node_b]
        else:
            graph[node_a].append(node_b)


        if node_b not in graph:
            graph[node_b] = [node_a]
        else:
            graph[node_b].append(node_a)




def graph_lines():
    graph = graphviz.Digraph()
    with open(in_file) as file:
        for line in file:
            """Custom iteration logic goes here"""
            line = line.strip()
            node_a, node_b = line.split("-")
            if node_a not in graph:
                graph.node(node_a)
            if node_b not in graph:
                graph.node(node_b)

    with open(in_file) as file:
        for line in file:
            node_a, node_b = line.split("-")
            graph.edge(node_a, node_b)

    return graph



def question_1():
    """Answer to the first question of the day"""
    answer = 0
    global graph

    for node in graph:
        for neighbour in graph[node]:
            for double_neighbour in graph[neighbour]:
                if double_neighbour == node: continue
                if node in graph[double_neighbour]:
                    if "t" == node[0] or "t" == neighbour[0] or "t" == double_neighbour[0]:
                        answer += 1

    return int(answer/6)


def question_2():
    """Answer to the second question of the day"""
    answer = 0

    # for node in graph:
    #     print(f"{node} - {find_cluster(node, [])}")

    return max([find_cluster(node, []) for node in graph])


def find_cluster(node, cluster):
    neighbours = graph[node]

    # check node is connected to existing cluster
    for cl in cluster:
        if cl == node: continue
        if cl not in neighbours:
            return len(cluster)
    cluster.append(node)

    return max([find_cluster(node, copy(cluster)) for node in neighbours if node not in cluster])





if __name__ == '__main__':
    # answer_1 = question_1()
    # print(f"Question 1 answer is: {answer_1}")

    answer_2 = question_2()
    print(f"Question 2 answer is: {answer_2}")
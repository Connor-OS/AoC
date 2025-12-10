TEST = False
in_file = "./resources/day_8_test.txt" if TEST else "./resources/day_8.txt"
from collections import defaultdict

from utils.input_handling import file_lines

def straight_line_dist(p1,p2):
    x1,y1,z1 = p1
    x2, y2, z2 = p2

    return ((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)**0.5


class Cluster:
    def __init__(self, points):
        self.points = [points[0], points[1]]

    def add_point(self, point):
        if point not in self.points:
            self.points.append(point)

    def merge(self, other):
        self.points.extend(other.points)
        self.points = list(set(self.points))

    def __len__(self):
        return len(self.points)

    def __gt__(self, other):
        return len(self.points) > len(other.points)

    def __contains__(self, point):
        if point in self.points:
            return True
        return False

    def __repr__(self):
        return (f"{self.points} {len(self.points)}")

def fetch_ordered_pairs():
    points = []
    for line in file_lines(in_file):

        x,y,z = line.split(",")
        points.append((int(x), int(y), int(z)))

    dists = {}
    for i, p1 in enumerate(points):
        for p2 in points[i+1:]:
            dists[straight_line_dist(p1,p2)] = (p1,p2)

    dists = sorted(dists.items(), key=lambda x: x[0])
    return [d[1] for d in dists]

def question_1():
    """Answer to the first question of the day"""

    pairs = fetch_ordered_pairs()

    if TEST: connections = 10
    else: connections = 1000

    pairs = pairs[:connections]

    clusters = [Cluster(pairs.pop(0))]

    for p1, p2 in pairs:
        clustered = False
        for cluster in clusters:
            if p1 in cluster and p2 not in cluster:
                if clustered:
                    cluster.merge(found_cluster)
                    clusters.remove(found_cluster)
                cluster.add_point(p2)
                found_cluster = cluster
                clustered = True
            if p2 in cluster and p1 not in cluster:
                if clustered:
                    cluster.merge(found_cluster)
                    clusters.remove(found_cluster)
                cluster.add_point(p1)
                found_cluster = cluster
                clustered = True

        if not clustered:
            clusters.append(Cluster([p1, p2]))


    clusters = (sorted(clusters, reverse=True))

    return len(clusters[0]) * len(clusters[1]) * len(clusters[2])


def question_2():
    """Answer to the second question of the day"""
    pairs = fetch_ordered_pairs()

    clusters = [Cluster(pairs.pop(0))]

    c = 0
    for p1, p2 in pairs:
        c += 1
        clustered = False
        for cluster in clusters:
            if p1 in cluster and p2 not in cluster:
                if clustered:
                    cluster.merge(found_cluster)
                    clusters.remove(found_cluster)
                cluster.add_point(p2)
                found_cluster = cluster
                clustered = True
            if p2 in cluster and p1 not in cluster:
                if clustered:
                    cluster.merge(found_cluster)
                    clusters.remove(found_cluster)
                cluster.add_point(p1)
                found_cluster = cluster
                clustered = True

        if not clustered:
            clusters.append(Cluster([p1, p2]))

        if any([len(c) == 1000 for c in clusters]):
            return p1[0] * p2[0]


    for cluster in clusters:
        print(cluster)
    return None
    # clusters = (sorted(clusters, reverse=True))



if __name__ == '__main__':
    answer_1 = question_1()
    print(f"Question 1 answer is: {answer_1}")

    answer_2 = question_2()
    print(f"Question 2 answer is: {answer_2}")

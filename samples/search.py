import bfs
from graph import Graph
import random


def print_path(path):
    for v in path:
        print v


def breadth_first_search(start, end):
    path = bfs.find_path(start, end.key)
    if not path:
        print "No path found between %s and %s" % (start, end)
        return
    path.reverse()
    print_path(path)


def dfs(graph):
    pass

if __name__ == '__main__':
    graph = Graph.random_graph()
    start = graph.vertices[random.randint(0, 9)]
    end = graph.vertices[random.randint(0, 9)]
    print "Start: %s, End: %s" % (start, end)
    breadth_first_search(start, end)

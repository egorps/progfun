import bfs
from graph import Graph
import random


def print_path(type, path, start, end):
    if not path:
        print "%s: No path found between %s and %s" % (type, start, end)
        return
    path.reverse()
    print "%s: " % type
    for v in path:
        print v


def breadth_first_search(start, end):
    path = bfs.find_path(start, end.key)
    print_path('BFS', path, start, end)


def depth_first_search(start, end):
    path = bfs.find_path(start, end.key)
    print_path('DFS', path, start, end)


if __name__ == '__main__':
    graph = Graph.random_graph()
    start = graph.vertices[random.randint(0, 9)]
    end = graph.vertices[random.randint(0, 9)]
    print "Start: %s, End: %s" % (start, end)
    breadth_first_search(start, end)
    depth_first_search(start, end)

import random
import datetime


class Vertex(object):

    def __init__(self, key):
        self.key = key
        self.neighbors = []

    def add_neighbor(self, vertex, cost=1):
        self.neighbors.append((vertex, cost))

    def get_neighbors(self):
        return self.neighbors

    def __str__(self):
        return "Vertex %d" % self.key


class Graph(object):

    def __init__(self, vertices):
        self.vertices = vertices

    @staticmethod
    def random_graph(num_vertices=10):
        random.seed(datetime.datetime.now())
        vertices = []
        for v in xrange(num_vertices):
            vertices.append(Vertex(random.randint(0,100)))
        graph = Graph(vertices)
        for v in vertices:
            num_neighbors = random.randint(0, 5)
            for n in xrange(num_neighbors):
                n_ix = random.randint(0, num_vertices -1)
                neighbor = vertices[n_ix]
                if neighbor.key != v.key and \
                    neighbor.key not in map(lambda x: x[0].key, v.get_neighbors()):
                    v.add_neighbor(vertices[n_ix])
                    neighbor.add_neighbor(v)

        return graph

    def __str__(self):
        return "DiGraph: %s" % [str(v) for v in self.vertices]


if __name__ == "__main__":
    g = Graph.random_graph()
    print g

    for v in g.vertices:
        print v, "neighbors:"
        for n in v.get_neighbors():
            print n[0]
        print

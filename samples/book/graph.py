class EdgeNode(object):

    def __init__(self, y, next_edge, weight=None):
        self.y = y
        self.next = next_edge
        self.weight = weight


class Graph(object):

    def __init__(self, n_vert, directed=False, max_edges=1000):
        self.nvertices = n_vert
        self.nedges = 0
        self.directed = directed
        self.edges = [None for _ in xrange(max_edges)]  # at each index an adjacency list for v_i resides

    def insert_edge(self, x, y, weight=1, directed=None):
        if directed is None:
            directed = self.directed

        # and edge in x's adjacency list
        p_old = self.edges[x]
        p = EdgeNode(y, p_old)
        self.edges[x] = p

        if not directed:
            self.insert_edge(y, x, weight, True)
        else:
            self.nedges += 1

    def __repr__(self):
        rep = ""
        for i in xrange(self.nvertices):
            rep += "%d:" % i
            p = self.edges[i]
            while p:
                rep += " %d" % p.y
                p = p.next
            rep += "\n"
        return rep


def read_graph(file_name, directed=False, weighted=False):
    """
    Read a graph from a file
    returns a graph

    :param file_name: the file from which the graph will be read.

    """

    def line_to_ints(line):
        print line
        return map(lambda x: int(x), line.split(' '))

    with open(file_name, 'r') as f:

        # read num vertices and number of edges from the file
        first_line = line_to_ints(f.readline())
        n_vert = first_line[0]
        n_edge = first_line[1]

        g = Graph(n_vert, directed)

        for i in xrange(n_edge):
            edge = line_to_ints(f.readline())
            weight = edge[2]if weighted else 1
            g.insert_edge(edge[0], edge[1], weight)

        return g

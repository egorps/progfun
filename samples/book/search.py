import graph

class SearchResult(object):

    def __init__(self, v, max_verts=1000):
        self.start = v
        self.discovered = [False for i in xrange(max_verts)]
        self.processed = [False for i in xrange(max_verts)]
        self.parent = [-1 for i in xrange(max_verts)]

    def discover(self, v):
        self.discovered[v] = True

    def is_discovered(self, v):
        return self.discovered[v]

    def is_processed(self, v):
        return self.processed[v]

    def process(self, v):
        self.processed[v] = True

    def set_parent(self, v, p):
        self.parent[v] = p

    def get_path(self, x):
        path = []
        while x != self.start:
            if x == -1:
                raise ValueError("no path from %d to %d", (self.start, x))
            path.insert(0, x)
            x = self.parent[x]

        path.insert(0, self.start)
        return path


def bfs(g, start):
    result = SearchResult(start)
    # just use a list since the built-in Queue library is
    # too complicated for this example
    q = [start]
    result.discover(start)

    while len(q) > 0:
        print len(q)
        v = q.pop(0)
        result.process(v)
        p = g.edges[v]
        while p:
            y = p.y
            if not result.is_discovered(y):
                result.discover(y)
                q.append(y)
                result.set_parent(y, v)
            p = p.next

    return result


def dfs(g, v, result=None):
    if not result:
        result = SearchResult(v)

    result.discover(v)

    p = g.edges[v]
    while p:
        y = p.y
        if not result.is_discovered(y):
            result.set_parent(y, v)
            result = dfs(g, y, result)

        p = p.next
    result.process(v)

    return result

if __name__ == '__main__':
   g = graph.read_graph('./graph.txt')
   print "Graph from file:\n", g
   bfs_result = bfs(g, 0)
   print "BFS Path to 7:", bfs_result.get_path(7)

   dfs_result = dfs(g, 0)
   print "DFS Path to 7:", dfs_result.get_path(7)

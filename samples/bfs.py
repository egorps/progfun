from Queue import LifoQueue


def find_path(vertex, key):
    visited = []
    queue = LifoQueue()
    queue.put([vertex])
    while not queue.empty():
        curr_path = queue.get()
        node = curr_path[0]
        if node.key == key:
            return curr_path

        visited.append(node.key)
        for n in node.get_neighbors():
            if n.key not in visited:
                queue.put([n] + curr_path)

    return None



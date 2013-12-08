

def find_path(vertex, key, depth=0):
    path = dfs(vertex, key, depth)
    return path if path else find_path(vertex, key, depth + 1)


def dfs(vertex, key, depth, path=[], cur_depth=0):
    new_path = [vertex] + path
    if vertex.key == key:
        return new_path
    if path < cur_depth:
        return dfs(vertex, key, depth, new_path, cur_depth + 1)
    return None


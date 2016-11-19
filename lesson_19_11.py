from homework_2 import Graph_2
from collections import deque
from collections import defaultdict
graph = Graph_2()
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(3, 4)
graph.add_edge(2, 5)
graph.add_edge(4, 5)

print('##########')
def reconstruct_path(paths, st, end):
    v = end
    path = [str(end)]
    while v != st:
        v = paths[v]
        path.append(str(v))
    return '-'.join(reversed(path)).lstrip()


def ShortPath(graph, st, end):
    queue = deque()
    parent = st
    paths = defaultdict(int)
    visited = set()
    visited.add(parent)
    queue.append(parent)
    while len(queue) > 0:
        parent = queue.popleft()
        neighbours = graph.neighbours(parent)
        for n in neighbours:
            if n not in visited:
                visited.add(n)
                queue.append(n)
                paths[n] = parent
    if end not in paths:
        return []
    return reconstruct_path(paths, st, end)


print(ShortPath(graph, 1, 4))

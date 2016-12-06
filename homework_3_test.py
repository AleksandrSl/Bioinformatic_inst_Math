import Homework_3 as g

graph = g.OrientedGraph()
graph.add_edge(1, 2)
graph.add_edge(3, 4)
graph.add_edge(2, 3)
graph.add_edge(6, 7)
graph.add_edge(7, 8)
graph.add_edge(8, 9)
graph.add_edge(9, 10)
graph.add_edge(10, 3)
graph.add_edge(10, 11)
graph.add_edge(11, 12)
graph.add_edge(12, 5)
graph.add_edge(11, 13)
graph.add_edge(13, 14)
graph.add_edge(4, 5)
graph.add_edge(5, 6)
graph.add_edge(14, 3)

# for n in graph.nodes.values():
#     print(n)

# print(graph.nodes)
graph.set_exit_time(1)
# print(graph.node_state)
graph.topology_sort()
print(graph.node_state)

for cycle in graph.cycles:
    print(' -> '.join(str(node.value) for node in cycle))

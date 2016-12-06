from collections import defaultdict

class Graph2:

    __slots__ = ['vertex_dict', 'edges']

    def __init__(self):
        self.vertex_dict = defaultdict(list)
        self.edges = 0

    def add_edge(self, v1, v2):
        self.vertex_dict[v1].append(v2)
        self.vertex_dict[v2].append(v1)
        self.edges += 1

    def del_edge(self, v1, v2):
        if v1 in self.vertex_dict:
            if v2 in self.vertex_dict[v1]:
                self.vertex_dict[v1].remove(v2)
                self.vertex_dict[v2].remove(v1)
                if self.vertex_dict[v1] == []:
                    self.vertex_dict.pop(v1)
                if self.vertex_dict[v2] == []:
                    self.vertex_dict.pop(v2)
                self.edges -= 1
        else:
            print("Edge doesn't exist")


    def neighbours(self, v):
        return self.vertex_dict[v]

    def vertices_list(self):
        return [v for v in self.vertex_dict]

    def size(self):
        len(self.vertex_dict)

    def size_str(self):
        return '{} edges {} vertices'.format(self.edges, len(self.vertex_dict))

    def __str__(self):
        output = []
        for v in self.vertex_dict:
            for neighbour in self.vertex_dict[v]:
                if neighbour > v:
                    output.append('{}-{}\n'.format(v, neighbour))
        return ''.join(output)

    def dfs(self):
        helper = DFShelper(g)
        helper.traverse(1)
        return helper.visited


class DFShelper:

    def __init__(self, g):
        self.graph = g
        self.visited = set()
        self.vertices_states = {v:[0]*2 for v in g.vertices_list()} #  Так делать нельзя

    def traverse(self, v, parent = None):
        self.vertices_states[v][0] = 1
        print(self.vertices_states)
        #print(v)
        if v not in self.visited:
            self.visited.add(v)
        for n in self.graph.neighbours(v):
            #print('n', n)
            if n not in self.visited:
                self.visited.add(n)
                self.traverse(n, v)
            if parent is not None and n != parent:
                print(v, n)
                self.has_cycle = (self.vertices_states[n][1] == 0)
        self.vertices_states[v][1] = 1

    # def has_cycle(self):
    #     for states in self.vertices_states.values():
    #         if states[0] == 1 and states[1] == 0:
    #             return True
    #     return False


g = Graph2()
g.add_edge(1,2)
g.add_edge(2,3)
g.add_edge(4,5)
g.add_edge(5,6)
g.add_edge(100, 101)
print(g)


g_w_cycle = Graph2()
g_w_cycle.add_edge(1,2)
g_w_cycle.add_edge(2,3)
g_w_cycle.add_edge(3,1)
g_w_cycle.add_edge(4,5)
g_w_cycle.add_edge(5,6)
g_w_cycle.add_edge(100, 101)
print(g)


def find_connect_comp(g):
    count = 0
    helper = DFShelper(g)
    for v in g.vertices_list():
        if v not in helper.visited:
            helper.traverse(v)
            print(helper.has_cycle)
            count += 1
    return count

print(find_connect_comp(g_w_cycle))


def find_cycles(g):
    count = 0
    helper = DFShelper(g)
    for v in g.vertices_list():
        if v not in helper.visited:
            helper.traverse(v)
            count += 1
    return count


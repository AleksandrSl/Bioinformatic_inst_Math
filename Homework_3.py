from collections import defaultdict, namedtuple
from itertools import chain

WeightedEdge = namedtuple('WeightedEdge', ['vertex', 'weight'])
# NodeState = namedtuple('Node', ['entry_time', 'exit_time'])


class INode:
    __slots__ = ['__value', '__index', ]

    def __init__(self, value, index):
        self.__value = value
        self.__index = index  # read-only

    @property
    def index(self):
        return self.__index

    @index.setter
    def index(self, index):
        self.__index = index

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value

    def __str__(self):
        return str(self.value)

    def __hash__(self):
        return hash(self.index)  # Не value, так как при упрощении графа в value оказывается список

    def __repr__(self):
        return 'Node({}, {})'.format(self.value, self.index)

    # @classmethod или лучше заменить __class__ на classmethod
    # def __deepcopy__(self, memodict={}):
    #     copy = self.__class__(self.value, self.index)
    #     copy.in_edges = self.in_edges[:]
    #     copy.out_edges = self.out_edges[:]
    #     return copy


class UnorientedNode(INode):

    __slots__ = ['__value', '__index', 'edges']

    def __init__(self, value, index):
        self.edges = defaultdict(int)
        super().__init__(value, index)

    def add_edge(self, node):
        self.edges[node] += 1

    def del_edge(self, node):
        if self.edges[node]:
            self.edges[node] -= 1
        else:
            self.edges.pop(node)

    def degree(self):
        return len(self.edges)

    def neighbours(self):
        return (node for node in self.edges)


class OrientedNode(INode):

    __slots__ = ['__value', '__index', 'out_edges', 'in_edges']

    def __init__(self, value, index):
        self.out_edges = defaultdict(int)
        self.in_edges = defaultdict(int)
        super().__init__(value, index)

    def add_out_edge(self, node):
        self.out_edges[node] += 1

    def add_in_edge(self, node):
        self.in_edges[node] += 1

    def del_out_edge(self, node):
        if self.out_edges[node]:
            self.out_edges[node] -= 1
        else:
            self.out_edges.pop(node)

    def del_in_edge(self, node):  # может будет чуть быстрее один раз присвоить self.out_edges[node] переменной
        if self.out_edges[node]:
            self.out_edges[node] -= 1
        else:
            self.out_edges.pop(node)

    def in_degree(self):
        return sum(self.in_edges.values())

    def out_degree(self):
        return sum(self.out_edges.values())

    def pop_out_edge(self):
        if not self.out_edges:
            return None, None
        return self.out_edges.popitem()

    def pop_in_edge(self):
        if not self.in_edges:
            return None, None
        return self.in_edges.popitem()

    def children_count(self):
        return len(self.out_edges)

    def parents_count(self):
        return len(self.in_edges)

    def neighbours_count(self):
        return self.parents_count() + self.children_count()

    def children(self):
        return (child for child in self.out_edges)

    def parents(self):
        return (parent for parent in self.in_edges)

    def neighbours(self):
        return chain(self.out_edges, self.in_edges)


class IGraph:

    __slots__ = ['nodes', 'length']

    def __init__(self):
        self.nodes = {}
        self.length = 0

    def add_edge(self, value1, value2):
        raise NotImplementedError

    def add_node(self, value):
        raise NotImplementedError

    def adjacency_list(self):
        raise NotImplementedError

    def get_node(self, value):
        raise NotImplementedError

    def __len__(self):
        return self.length


class OrientedGraph(IGraph):

    __slots__ = ['nodes', 'cycles', 'node_state', 'length']

    def __init__(self):
        self.cycles = []
        self.node_state = None
        super().__init__()

    def find_start(self):
        for n in self.nodes.values():
            if n.in_degree == 0:
                return n
        return None

    def add_edge(self, value1, value2):
        node1 = self.get_node(value1)
        node2 = self.get_node(value2)
        node1.add_out_edge(node2)
        node2.add_in_edge(node1)

    def add_node(self, value):
        self.nodes[value] = OrientedNode(value, len(self.nodes) + 1)
        self.length += 1

    def get_node(self, value):
        if value not in self.nodes:
            self.add_node(value)
        return self.nodes[value]

    def adjacency_list(self):
        raise NotImplementedError

    def set_exit_time(self, start_value=None):
        if start_value is None:
            start_node = self.find_start()
        else:
            start_node = self.get_node(start_value)

        self.node_state = {n: [0] * 2 for n in self.nodes.values()}
        path = []
        time = 1

        def dfs(n):
            nonlocal time
            # print(path)
            for n in n.children():
                path.append(n)
                if not self.node_state[n][0]:
                    self.node_state[n][0] = 1
                elif not self.node_state[n][1]:
                    self.cycles.append(path[path.index(n):])
                    return
                dfs(n)
                self.node_state[n][1] = time
                time += 1
                path.pop()

        self.node_state[start_node][0] = 1
        path.append(start_node)
        dfs(start_node)
        self.node_state[start_node][1] = time

    def topology_sort(self):
        if self.cycles:
            print('No topology sort is avaliable since graph has cycles')
            return None
        for node in self.nodes.values():
            node.index = self.length - self.node_state[node][1]


class UnorientedGraph(IGraph):

    def add_edge(self, value1, value2):
        node1 = self.get_node(value1)
        node2 = self.get_node(value2)
        node1.add_edge(node2)
        node2.add_edge(node1)

    def add_node(self, value):
        self.nodes[value] = UnorientedNode(value, len(self.nodes) + 1)

    def get_node(self, value):
        if value not in self.nodes:
            self.add_node(value)
        return self.nodes[value]

    def adjacency_list(self):
        raise NotImplementedError

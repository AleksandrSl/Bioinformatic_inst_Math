from collections import defaultdict
from bisect import bisect_right

class Node:
    __slots__ = ['value']

    def __init__(self, value):
        self.value = None

    def add_value(self, value):
        self.value = value

    # def add_neighbour(self, Node):
    #     self.neigbours.append(Node)

    def __str__(self):
        return str(self.value)

    def __hash__(self):
        return hash(self.value)

class Graph3:

    def __init__(self):
        self.graph = {}
        self.i = 0

    def add_edge(self, Node1, Node2):
        self.add_vertex(Node1)
        self.add_vertex(Node2)
        self.i += 1

    def add_vertex(self, Node):
        if Node not in self.graph: # Возможно немного странно, что это здесь проверяется
            self.graph[Node] = {'in': [], 'out': []}



d = defaultdict(Node)
d[1].add_value(5)
print(d[1])
# class Graph:  # Сплошные костыли, но удалять вершины должен правильно, и выписывать ребра удобно. Вообще переделать надо(
#
#     __slots__ = ['vertex_dict_l', 'vertex_dict_r', 'edges', 'vertices']
#
#     def __init__(self):
#         self.vertex_dict_l = defaultdict(list)
#         self.vertex_dict_r = defaultdict(list)
#         self.vertices = defaultdict(int)
#         self.edges = 0
#
#     def add_edge(self, v1, v2):
#         self.vertex_dict_l[v1].append(v2)
#         self.vertex_dict_r[v2].append(v1)
#         self.edges += 1
#         self.vertices[v1] += 1
#         self.vertices[v2] += 1
#
#     def del_edge(self, v1, v2):
#         if v1 in self.vertex_dict_l and v2 in self.vertex_dict_l[v1]:
#             self.vertex_dict_l[v1].remove(v2)
#         elif v2 in self.vertex_dict_r and v1 in self.vertex_dict_l[v2]:
#             self.vertex_dict_r[v2].remove(v1)
#         else:
#             print("Edge doesn't exist")
#             return
#         self.edges -= 1
#         self.vertices[v1] -= 1
#         self.vertices[v2] -= 1
#
#     def neighbours(self, v):
#         return self.vertex_dict_l[v] + self.vertex_dict_r[v]
#
#     def vertices_list(self):
#         return [v for v in self.vertices if self.vertices[v] != 0]
#
#     def size(self):
#         return '{} edges {} vertices'.format(self.edges, len(self.vertices_list()))
#
#     def __str__(self):
#         output = []
#         for v in self.vertex_dict_l:
#             for neighbour in self.vertex_dict_l[v]:
#                 output.append('{}-{}\n'.format(v, neighbour))
#         return ''.join(output)




class Stack:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def top(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def size(self):
        return len(self.items)


class DoubleStack:

    def __init__(self, n):
        self.items = ['_'] * n
        self.first_head = 0
        self.second_head = -1

    def is_full(self):
        return self.first_head - self.second_head > len(self.items)

    def is_first_empty(self):
        return self.first_head == 0

    def is_second_empty(self):
        return self.second_head == -1

    def push_first(self, item):
        if not self.is_full():
            self.items[self.first_head] = item
            self.first_head += 1
        else:
            print('Stack is full')

    def push_second(self, item):
        if not self.is_full():
            self.items[self.second_head] = item
            self.second_head -= 1
        else:
            print('Stack is full')

    def pop_first(self):
        if self.is_first_empty():
            return None
        t = self.items[self.first_head - 1]
        self.items[self.first_head - 1] = '_'
        self.first_head -= 1
        return t

    def pop_second(self):
        if self.is_second_empty():
            return None
        t = self.items[self.second_head + 1]
        self.items[self.second_head + 1] = '_'
        self.second_head += 1
        return t

    def __str__(self):
        return str(self.items)


def is_braces_right(braces_string):
    stack = Stack()
    for brace in braces_string:
        if brace == '(':
            stack.push(1)
        elif brace == ')':
            flag = stack.pop()
            if flag is None:
                return False
    if not stack.is_empty():
        return False
    return True


def magic_func(l, x): # Додумался сам
    """
    Return True if there are a and b in l, such that a + b = x
    :param l:
    :param x:
    :return:
    """
    l.sort()  # nlogn
    for i in (i - x for i in l):
        print(i)
        if -i == l[bisect_right(l, i) - 1]: # logn # Самому писать bisection_search лень в 4 утра уже(
            return True
    return False


def magic_func_2(l, x): # Посмотрел в интернете
    """
        Return True if there are a and b in l, such that a + b = x
        :param l:
        :param x:
        :return:
    """
    l.sort()
    ind_1 = 0
    ind_2 = len(l) -1
    while ind_1 != ind_2:
        y = l[ind_1] + l[ind_2]
        if y == x:
            return True
        elif y > x:
            ind_2 -= 1
        else:
            ind_1 += 1
    return False
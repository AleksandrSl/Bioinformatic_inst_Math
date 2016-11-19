from collections import defaultdict
from bisect import bisect_right
# class Node:
#     __slots__ = 'neigbours'
#
#     def __init__(self, value):
#         self.value =


class Graph:  # Сплошные костыли, но удалять вершины должен правильно, и выписывать ребра удобно. Вообще переделать надо(

    __slots__ = ['vertex_dict_l', 'vertex_dict_r', 'edges', 'vertices']

    def __init__(self):
        self.vertex_dict_l = defaultdict(list)
        self.vertex_dict_r = defaultdict(list)
        self.vertices = defaultdict(int)
        self.edges = 0

    def add_edge(self, v1, v2):
        self.vertex_dict_l[v1].append(v2)
        self.vertex_dict_r[v2].append(v1)
        self.edges += 1
        self.vertices[v1] += 1
        self.vertices[v2] += 1

    def del_edge(self, v1, v2):
        if v1 in self.vertex_dict_l and v2 in self.vertex_dict_l[v1]:
            self.vertex_dict_l[v1].remove(v2)
        elif v2 in self.vertex_dict_r and v1 in self.vertex_dict_l[v2]:
            self.vertex_dict_r[v2].remove(v1)
        else:
            print("Edge doesn't exist")
            return
        self.edges -= 1
        self.vertices[v1] -= 1
        self.vertices[v2] -= 1

    def neighbours(self, v):
        return self.vertex_dict_l[v] + self.vertex_dict_r[v]

    def vertices_list(self):
        return [v for v in self.vertices if self.vertices[v] != 0]

    def size(self):
        return '{} edges {} vertices'.format(self.edges, len(self.vertices_list()))

    def __str__(self):
        output = []
        for v in self.vertex_dict_l:
            for neighbour in self.vertex_dict_l[v]:
                output.append('{}-{}\n'.format(v, neighbour))
        return ''.join(output)

class Graph_2:  # Сплошные костыли, но удалять вершины должен правильно, и выписывать ребра удобно. Вообще переделать надо(

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
        return [v for v in self.vertices if self.vertices[v] != 0]

    def size(self):
        return '{} edges {} vertices'.format(self.edges, len(self.vertex_dict))

    def __str__(self):
        pass

graph = Graph()
graph.add_edge(1, 3)
graph.add_edge(3, 2)
graph.add_edge(4, 5)
graph.add_edge(1, 6)
graph.add_edge(1, 5)
print(graph.neighbours(1))
print(graph.size())
print(graph)

graph = Graph_2()
graph.add_edge(1, 3)
graph.add_edge(3, 2)
graph.add_edge(4, 5)
graph.add_edge(1, 6)
graph.add_edge(1, 5)
print(graph.neighbours(1))
print(graph.size())
# print(graph)

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
        self.first_head  -= 1
        self.items[self.first_head - 1] = 0
        return t

    def pop_second(self):
        if self.is_second_empty():
            return None
        t = self.items[self.second_head + 1]
        self.second_head += 1
        self.items[self.second_head + 1] = 0
        return t

    def __str__(self):
        return str(self.items)

print("#####################_______DoubleStack_______#######################")
ds = DoubleStack(10)
ds.push_first(10)
ds.push_second(100)
for i in range(9):
    ds.push_first(i)
print(ds)
print(ds.pop_first())
print(ds.pop_first())
print("#####################_______END_______#######################")

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

braces_1 = '((()))((()))((()))' # True
braces_2 = '((()))((()))((())'  # False
assert is_braces_right(braces_1) == True
assert is_braces_right(braces_2) == False
assert is_braces_right('') == True
assert is_braces_right('()') == True
assert is_braces_right(')(') == False

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

assert magic_func([1,2,3,4], 5) == True
assert magic_func([1,2,3,4], 100) == False
assert magic_func([1,2], 2) == False

assert magic_func_2([1,2,3,4], 5) == True
assert magic_func_2([1,2,3,4], 100) == False


# import inspect
# print(inspect.findsource(bisect_right))
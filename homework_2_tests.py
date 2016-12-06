import homework_2 as hw2
# print("#####################_______Graph_______#######################")
# graph = hw2.Graph()
# graph.add_edge(1, 3)
# graph.add_edge(3, 2)
# graph.add_edge(4, 5)
# graph.add_edge(1, 6)
# graph.add_edge(1, 5)
# print(graph.neighbours(1))
# print(graph.size())
# print(graph)
# print("#####################_______END_______#######################")

print("#####################_______Graph2_______#######################")
graph = hw2.Graph2()
graph.add_edge(1, 3)
graph.add_edge(3, 2)
graph.add_edge(4, 5)
graph.add_edge(1, 6)
graph.add_edge(1, 5)
print(graph.neighbours(1))
print(graph.size())
print(graph)
print("#####################_______END_______#######################")


# print("#####################_______DoubleStack_______#######################")
# ds = hw2.DoubleStack(10)
# ds.push_first(10)
# ds.push_second(100)
# for i in range(9):
#     ds.push_first(i)
# print(ds)
# for _ in range(9):
#     print(ds.pop_first())
# print(ds.pop_first())
# print(ds.pop_second())
# print(ds.pop_second())
# print("#####################_______END_______#######################")
#
# print("#####################_______Braces_______#######################")
# braces_1 = '((()))((()))((()))' # True
# braces_2 = '((()))((()))((())'  # False
# assert hw2.is_braces_right(braces_1) == True
# assert hw2.is_braces_right(braces_2) == False
# assert hw2.is_braces_right('') == True
# assert hw2.is_braces_right('()') == True
# assert hw2.is_braces_right(')(') == False
# print("#####################_______END_______#######################")
#
# print("#####################_______Magic_func_______#######################")
# assert hw2.magic_func([1,2,3,4], 5) == True
# assert hw2.magic_func([1,2,3,4], 100) == False
# assert hw2.magic_func([1,2], 2) == False
#
# assert hw2.magic_func_2([1,2,3,4], 5) == True
# assert hw2.magic_func_2([1,2,3,4], 100) == False
# print("#####################_______END_______#######################")
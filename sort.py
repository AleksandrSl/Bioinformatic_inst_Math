from functools import partial
from first_blood import timethis
from random import shuffle
def merge(l1, l2, order):
    # print('l1, l2 is: {}, {}'.format(l1, l2))
    new_l = []
    # This takes most of the time
    if order == 'increase':     # не хорошо конечно, что это каждый раз вызывается
        comp_func = int.__gt__  # и вообще в идеале независящим от типа надо делать
    elif order == 'decrease':
        comp_func = int.__lt__

    while l1 and l2:
        if comp_func(l1[0], l2[0]):  # pop(0) работает за O(n^2 * logn), но вообще не похоже на то
            new_l.append(l2.pop(0))
        else:
            new_l.append(l1.pop(0))

    if l1:
        new_l.extend(l1)
    elif l2:
        new_l.extend(l2)
    return new_l


def merge_v2(l1, l2, order): # работает за logn*n
    # print('l1, l2 is: {}, {}'.format(l1, l2))
    new_l = []
    i1 = 0
    i2 = 0

    if order == 'increase':     # не хорошо конечно, что это каждый раз вызывается
        comp_func = int.__gt__  # и вообще в идеале независящим от типа надо делать
    elif order == 'decrease':
        comp_func = int.__lt__

    while i1 != len(l1) and i2 != len(l2):
        if comp_func(l1[i1], l2[i2]):
            new_l.append(l2[i2])
            i2 += 1
        else:
            new_l.append(l1[i1])
            i1 += 1

    new_l.extend(l1[i1:])
    new_l.extend(l2[i2:])
    return new_l


# import pdb
def merge_sort(l, order='increase'):
    # pdb.set_trace()
    if len(l) == 1 or len(l) == 0:
        return l
    m = len(l)//2
    # merge_sort_with_order = partial(merge_sort, order=order)
    return merge(merge_sort(l[:m], order), merge_sort(l[m:], order), order)

def merge_sort_v2(l, order='increase'):
    # pdb.set_trace()
    if len(l) == 1 or len(l) == 0:
        return l
    m = len(l)//2
    # merge_sort_with_order = partial(merge_sort, order=order)
    return merge_v2(merge_sort(l[:m], order), merge_sort(l[m:], order), order)


def min_with_pos(l):
    min = l[0]
    ind = 0
    for i, el in enumerate(l):
        if el < min:
            min = el
            ind = i
    return min, ind


def selection_sort(l):  # уничтожает исходный список
    new_l = []
    while l:
        _, ind = min_with_pos(l)
        new_l.append(l.pop(ind))
    return new_l


def selection_sort_v2(l): # сортирует исходный список
    for i in range(len(l)):
        min_, ind = min_with_pos(l[i:])
        l[i], l[ind + i] = min_, l[i]
    return l

''' Сложность сортировки выбором!!!!!!!!
Мы n раз вызываем функцию поиска минимума, эта функция работает за время n, так как на каждой итерации список,
 в котором мы ищем минимум скоращается на один, мы получаем что сумма времен всех вызовов будет равна сумме
  арифметической прогрессии (n + 1)*n/2 = (n^2 + n)/2. В целом, учитывая тот факт, что на самом деле операций
  больше чем n в несколько раз, деление 2 мы можем спокойно опустить, и получим сложность алгоритма О(n^2).
  В худшем случае и в лучшем случае время работы остается одинаковым, так как поиск минимума всегда будет идти
  за одно и то же время.
'''

def boyer_moore_majority(l):
    maj = None
    count = 1
    for el in l:
        if el == maj:
            count += 1
        else:
            count -= 1
            if count == 0:
                count = 1
                maj = el
    return maj if l.count(maj) > len(l) / 2 else None


# def choice_sort_v2(l):
#     new_l = []
#     for _ in range(len(l)):
#         min_, ind = min_with_pos(l)
#         print(min_, ind)
#         new_l.append(min_)
#         l[:ind].extend(l[ind+1:])
#         print(l)
#     return new_l
@timethis
def run_v1(l):
    return merge_sort(l)

@timethis
def run_v2(l):
    return merge_sort_v2(l)

@timethis
def run_sel_v1(l):
    return selection_sort(l)

@timethis
def run_stand(l):
    return sorted(l)


large_l = list(range(100000))
shuffle(large_l)
print('shuffled')
l1 = run_v1(large_l)
l2 = run_v2(large_l)
l4 = run_stand(large_l)
#l3 = run_sel_v1(large_l)
assert l1 == list(range(10000))
#assert l1 == l2 == l3 == l4

def bubble_sort(l):
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(len(l) - 1):
            if l[i] > l[i + 1]:
                l[i + 1], l[i] = l[i], l[i + 1]
                is_sorted = False
    return l


import math

print(math.exp(1.61)/(1 + math.exp(1.61)))

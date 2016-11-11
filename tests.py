import unittest as unit
import sort
import itertools
from first_blood import timethis
from random import shuffle
# first_blood tests
#####################################
# import first_blood as fb
# print(fb.find_max_product_optim_v2([40, 1, 2, 30, 30]))
#
# print('1', fb.find_motif('ATGCGCGGCGCGCGCGCGCGCGATATATATGCTCGC', 'GCGGC'))
# finder = fb.Finder()
# finder2 = fb.Finder2(5)
# print(finder.find_motif_hash('ATGCGCGGCGCGCGCGCGCGCGATATATATGCTCGC', 'GCGGC'))
# print(finder2.find_motif_hash_v1('ATGCGCGGCGCGCGCGCGCGCGATATATATGCTCGC', 'GCGGC'))
# print(finder2.find_motif_hash_v2('ATGCGCGGCGCGCGCGCGCGCGATATATATGCTCGC', 'GCGGC'))
#######################################

#homework_1 tests
######################################
# from sys import setrecursionlimit
# import  homework_1
# setrecursionlimit(1000000)
# print(homework_1.run_fib_recursive(40))
# for i in range(1, 100):
# print(homework_1.fibonacci_dynamical(i))
# print(homework_1.run_lambda_fib(40))
# print(homework_1.run_fib_recursive(40))
# fib = homework_1.FibRecursive()
# print(fib.fibonacci_recursive_v2(7))
# print(fib.count)
##############################################
large_l = [el for el in range(100000)]
shuffle(large_l)


class TestMergeSortIncrease(unit.TestCase):

    # @timethis
    def test_simple(self):
        main_l = [1, 2, 3, 4, 5, 6]
        for l in itertools.permutations(main_l):
            with self.subTest(l=l):
                self.assertListEqual(sort.merge_sort(list(l), order='increase'), main_l)

    def test_empty(self):
        self.assertListEqual(sort.merge_sort(list([]), order='increase'), [])

    def test_repeating_el(self):
        main_l = [1, 2, 3, 3, 4, 5, 6, 6]
        for l in itertools.permutations(main_l):
            with self.subTest(l=l):
                self.assertListEqual(sort.merge_sort(list(l), order='increase'), main_l)

    @timethis
    def test_large_sample(self):
        global large_l
        print('Merge sort')
        sort.merge_sort(large_l)

class TestMergeSortDecrease(unit.TestCase):

    # @timethis
    def test_simple(self):
        main_l = [1, 2, 3, 4, 5, 6]
        main_l.sort(reverse=True)
        for l in itertools.permutations(main_l):
            with self.subTest(l=l):
                self.assertListEqual(sort.merge_sort(list(l), order='decrease'), main_l)

    def test_empty(self):
        self.assertListEqual(sort.merge_sort(list(), order='decrease'), [])

    def test_repeating_el(self):
        main_l = [1, 2, 3, 3, 4, 5, 6, 6]
        main_l.sort(reverse=True)
        for l in itertools.permutations(main_l):
            with self.subTest(l=l):
                self.assertListEqual(sort.merge_sort(list(l), order='decrease'), main_l)

class TestChoiceSort(unit.TestCase):

    # @timethis
    def test_simple(self):
        main_l = [1, 2, 3, 4, 5, 6]
        for l in itertools.permutations(main_l):
            with self.subTest(l=l):
                self.assertListEqual(sort.choice_sort(list(l)), main_l)

    def test_empty(self):
        self.assertListEqual(sort.choice_sort(list()), [])

    def test_repeating_el(self):
        main_l = [1, 2, 3, 3, 4, 5, 6, 6]
        for l in itertools.permutations(main_l):
            with self.subTest(l=l):
                self.assertListEqual(sort.choice_sort(list(l)), main_l)

    @timethis
    def test_large_sample(self):
        global large_l
        print('Choice_sort')
        sort.choice_sort(large_l)


if __name__ == '__main__':
    unit.main()
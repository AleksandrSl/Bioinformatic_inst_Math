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
from sys import setrecursionlimit
import  homework_1
setrecursionlimit(1000000)
# print(homework_1.run_fib_recursive(40))
#for i in range(1, 100):
#    print(homework_1.fibonacci_dynamical(i))



def sum(n):
   if n == 1:
       return 1
   else:
       return n + sum(n - 1)

print(sum(3))

n=100
from math import factorial, log2, log, sqrt
import pylab
pylab.plot(factorial(n))
# print(factorial(n))
# print(2**n)
# print(4**n)
# print(2**(3*n))
# print(round(n**(n**0.5)))
# print(round(n**(log2(n))))
# #print(round(2**(2**n)))
# print(round(2**n))
# print('#######3')
# print(round(log2(n)**(log2(n))))
# print(round(7**(log2(n))))
# print(round(3**(log2(n))))
# print(round(n**2))
# # print(round(log2(n)**2))
# print(round(log2(factorial(n))))
# print(round(log2(log2(n))))
# print(round(sqrt(log(n, 4))))
# print(round(n/(log(n, 5))))
# print(round(log(n, 3)))
# print(3**10)
# print(round(sqrt(n)))

#print(homework_1.run_lambda_fib(40))
#print(homework_1.run_fib_recursive(40))

fib = homework_1.FibRecursive()
print(fib.fibonacci_recursive_v2(7))
print(fib.count)
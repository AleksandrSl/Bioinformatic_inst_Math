from first_blood import timethis

#########First Task
def sum_up_to_n(n):
    if n == 0:
        return 0
    return n + sum_up_to_n(n - 1)


#########Second Task
def fibonacci_recursive(n): # Time complexity O(2^n)
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


class FibRecursive:
    def __init__(self):
        self.count = 0

    def fibonacci_recursive_v2(self, n): # Time complexity O(2^n)
        self.count += 1
        if n <= 1:
            return n
        return self.fibonacci_recursive_v2(n - 1) + self.fibonacci_recursive_v2(n - 2)


#########Third Task
@timethis
def fibonacci_dynamical(n): # Time complexity O(n)
    if n == 1 or n == 2:
        return 1
    fib1 = 1
    fib2 = 1
    for _ in range(2, n):
        fib = fib1 + fib2
        fib2, fib1 = fib, fib2
    return fib


@timethis
def run_lambda_fib(n):
    l = lambda n: l(n-1) + l(n-2) if n > 1 else n
    return l(n)


@timethis
def run_fib_recursive(n):
    return fibonacci_recursive(n)
from functools import reduce
from sympy import factorint, lcm

def A001175(n):
    """See https://oeis.org/A001175"""
    if n == 1:
        return 1
    f = factorint(n)
    if len(f) > 1:
        return reduce(lcm, (A001175(a**f[a]) for a in f))

    else:
        k, x = 1, [1, 1]
        while x != [0, 1]:
            k += 1
            x = [x[1], (x[0]+x[1]) % n]
        return k # Chai Wah Wu, Jul 17 2019

def fib(n):
    if n == 0:
        return 0
    fibs = [0 , 1]
    for _ in range(n-1):
        fibs = [fibs[1], fibs[0] + fibs[1]]
    return fibs[1]

def fib_mod(n, m):
    """Get nth Fibonacci number modulo m"""
    n %= A001175(m)
    return fib(n) % m


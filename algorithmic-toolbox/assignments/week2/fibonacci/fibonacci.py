# Uses python2

import numpy as np


DEBUG = False


def fib(n):
    assert n >= 0
    i, j = 0, 1
    for _ in xrange(n):
        i, j = j, i+j
    return i


def fib_naive(n):
    return n if n < 2 else fib_naive(n-1) + fib_naive(n-2)


def stress_test(max_n):
    assert max_n >= 0
    while True:
        n = np.random.randint(0, max_n+1)
        x, y = fib(n), fib_naive(n)
        if x != y:
            print('test failed', x, y)
            raise
        print('test passed')


def main():
    if DEBUG:
        stress_test(max_n=20)
    else:
        n = int(raw_input())
        print(fib(n))


if __name__ == '__main__':
    main()

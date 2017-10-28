# Uses python2


import numpy as np

DEBUG = False


def solve(n, m):
    period_len = 1
    i, j = 0, 1
    while not (i == 1 and j == 0):
        period_len += 1
        i, j = j, i+j
        i %= m
        j %= m
    n %= period_len
    i, j = 0, 1
    for _ in xrange(n):
        i, j = j, i+j
        i %= m
        j %= m
    return i % m


def fib(n):
    assert n >= 0
    i, j = 0, 1
    for _ in xrange(n):
        i, j = j, i+j
    return i


def solve_naive(n, m):
    return fib(n) % m


def stress_test(max_n):
    while True:
        n = np.random.randint(1, max_n+1)
        m = np.random.randint(2, max_n+1)
        # n, m = 4, 2
        x, y = solve(n, m), solve_naive(n, m)
        if x != y:
            print('test failed: n={}, m={}, x={}, y={}'.format(n, m, x, y))
            raise
        print 'test passed'


def main():
    if DEBUG:
        stress_test(max_n=10000)
    else:
        n, m = map(int, raw_input().split())
        print(solve(n, m))


if __name__ == '__main__':
    main()
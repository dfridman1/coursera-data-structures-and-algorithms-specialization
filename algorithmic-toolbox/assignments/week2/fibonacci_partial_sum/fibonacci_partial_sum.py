# Uses python2


import numpy as np


DEBUG = False


def solve(m, n):
    n = _solve(n)
    if m > 0:
        m = _solve(m-1)
    return (10 + n - m) % 10


def _solve(n):
    period_len = 1
    i, j, s = 0, 1, 0
    while not (i == 1 and j == 0):
        period_len += 1
        i, j = j, i+j
        s += i
        i %= 10
        j %= 10
        s %= 10
    d = n // period_len
    s = (s * d) % 10
    n %= period_len
    i, j = 0, 1
    for _ in xrange(n):
        i, j = j, i+j
        s += i
        i %= 10
        j %= 10
        s %= 10
    return s


def _solve_naive(n):
    i, j, s = 0, 1, 0
    for _ in xrange(n):
        i, j = j, i+j
        s += i
    return s % 10


def solve_naive(m, n):
    n = _solve_naive(n)
    if m > 0:
        m = _solve_naive(m-1)
    return (10 + n - m) % 10


def stress_test(max_n):
    while True:
        n = np.random.randint(0, max_n+1)
        m = np.random.randint(0, n+1)
        m, n = 1, 3
        x, y = solve(m, n), solve_naive(m, n)
        if x != y:
            print('test failed: m={}, n={}, x={}, y={}'.format(m, n, x, y))
            raise
        print('test passed')


def main():
    if DEBUG:
        stress_test(max_n=10000)
    else:
        m, n = map(int, raw_input().split())
        print(solve(m, n))


if __name__ == '__main__':
    main()

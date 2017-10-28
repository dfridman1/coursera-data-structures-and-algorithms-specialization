# Uses python2


import numpy as np


DEBUG = False


def solve(n):
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


def solve_naive(n):
    i, j, s = 0, 1, 0
    for _ in xrange(n):
        i, j = j, i+j
        s += i
    return s % 10


def stress_test(max_n):
    while True:
        n = np.random.randint(0, max_n+1)
        x, y = solve(n), solve_naive(n)
        if x != y:
            print('test failed: n={}, x={}, y={}'.format(n, x, y))
            raise
        print('test passed')


def main():
    if DEBUG:
        stress_test(max_n=100000)
    else:
        n = int(raw_input())
        print(solve(n))


if __name__ == '__main__':
    main()

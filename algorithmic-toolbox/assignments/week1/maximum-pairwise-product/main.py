# Uses python2


import numpy as np


DEBUG = False


def solve(xs):
    assert len(xs) > 1
    max_i = 0
    for i in xrange(1, len(xs)):
        if xs[i] > xs[max_i]:
            max_i = i
    second_max_i = 1 if max_i == 0 else 0
    for i in xrange(len(xs)):
        if i != max_i and xs[i] > xs[second_max_i]:
            second_max_i = i
    return xs[max_i] * xs[second_max_i]


def naive_solve(xs):
    assert len(xs) > 1
    ans = -float('inf')
    for i in xrange(len(xs)):
        for j in xrange(i):
            ans = max(ans, xs[i]*xs[j])
    return ans


def _generate_random_vector(size):
    assert size > 0
    return np.random.randint(0, 100000, size=size)


def stress_test(max_size=100):
    while True:
        size = np.random.randint(2, max_size+1)
        v = _generate_random_vector(size)
        x, y = solve(v), naive_solve(v)
        if x != y:
            print('test failed', x, y)
        print 'test passed'


def _read_input():
    n = int(raw_input())
    xs = map(int, raw_input().split())
    return n, xs


def main():
    if DEBUG:
        stress_test(max_size=100)
    else:
        n, xs = _read_input()
        ans = solve(xs)
        print(ans)


if __name__ == '__main__':
    main()

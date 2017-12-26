# Uses python2


import numpy as np


DEBUG = False


def majority_exists(xs):
    median = order_statistic(xs, len(xs) // 2)
    cnt = 0
    for x in xs:
        if x == median:
            cnt += 1
    return int(cnt > len(xs) // 2)


def order_statistic(lst, k):
    assert 0 <= k < len(lst)
    def _order_statistic(p, r):
        assert p <= r
        a, b = partition(lst, p, r)
        if k < a:
            res = _order_statistic(p, a-1)
        elif k > b:
            res = _order_statistic(b+1, r)
        else:
            res = lst[a]
        return res

    return _order_statistic(0, len(lst)-1)


def order_statistic_naive(lst, k):
    assert 0 <= k < len(lst)
    return sorted(lst)[k]


def swap(lst, i, j):
    lst[i], lst[j] = lst[j], lst[i]


def partition(xs, p, r):
    pivot_idx = np.random.randint(p, r+1)
    pivot = xs[pivot_idx]
    swap(xs, pivot_idx, r)
    i = j = k = p
    while k < r:
        if xs[k] == pivot:
            swap(xs, k, j)
            j += 1
        elif xs[k] < pivot:
            swap(xs, k, j)
            swap(xs, j, i)
            i += 1
            j += 1
        k += 1
    swap(xs, j, r)
    return i, j


def stress_test(max_size):
    gen = lambda: list(np.random.randint(-1000, 1000, size=np.random.randint(1, max_size+1)))
    while True:
        xs = gen()
        ys = [x for x in xs]
        k = np.random.randint(0, len(xs))
        x = order_statistic_naive(xs, k)
        y = order_statistic(xs, k)

        if x != y:
            print ys, k
            print('test failed', x, y)
            raise
        print('test passed')


def main():
    if DEBUG:
        stress_test(max_size=1000)
    else:
        raw_input()
        xs = map(int, raw_input().split())
        print(majority_exists(xs))


if __name__ == '__main__':
    main()

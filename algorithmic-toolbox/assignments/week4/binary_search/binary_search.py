# Uses python2

import numpy as np


DEBUG = False


def bin_search(lst, key):
    lo, hi = 0, len(lst)-1
    while lo < hi:
        mid = (lo + hi) >> 1
        if lst[mid] < key:
            lo = mid+1
        else:
            hi = mid
    if lo == hi and lst[lo] == key:
        index = lo
    else:
        index = -1
    return index


def linear_search(lst, key):
    index = -1
    for i, x in enumerate(lst):
        if x == key:
            index = i
            break
    return index


def stress_test(max_size):
    while True:
        size = np.random.randint(1, max_size+1)
        xs = sorted(np.random.randint(-1000, 1000, size=size))
        if np.random.randint(0, 2) == 0:
            k = np.random.choice(xs)
        else:
            k = np.random.randint(-1000, 1000)
        x, y = bin_search(xs, k), linear_search(xs, k)
        if x != y:
            print('test failed', x, y)
            raise
        print('test passed')


def main():
    if DEBUG:
        stress_test(max_size=1000)
    else:
        xs = map(int, raw_input().split())[1:]
        xs = sorted(xs)
        ks = map(int, raw_input().split())[1:]
        indices = [bin_search(xs, k) for k in ks]
        print(' '.join(map(str, indices)))



if __name__ == '__main__':
    main()

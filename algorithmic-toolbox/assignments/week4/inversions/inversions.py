# Uses python2

import numpy as np


DEBUG = False


def count_inversions(xs):
    def _count_inversions(xs):
        if len(xs) < 2:
            return xs, 0
        else:
            mid = len(xs) >> 1
            left, left_count = _count_inversions(xs[:mid])
            right, right_count = _count_inversions(xs[mid:])
            cross, cross_count = merge(left, right)
            return cross, left_count + right_count + cross_count
    _, num_inversions = _count_inversions(xs)
    return num_inversions


def merge(xs, ys):
    merged = []
    i = j = count = 0
    while i < len(xs) and j < len(ys):
        if xs[i] > ys[j]:
            count += len(xs) - i
            merged.append(ys[j])
            j += 1
        else:
            merged.append(xs[i])
            i += 1
    while i < len(xs):
        merged.append(xs[i])
        i += 1
    while j < len(ys):
        merged.append(ys[j])
        j += 1
    return merged, count


def count_inversions_naive(xs):
    cnt = 0
    for j in xrange(len(xs)):
        for i in xrange(j):
            if xs[i] > xs[j]:
                cnt += 1
    return cnt


def stress_test(max_size):
    while True:
        xs = list(np.random.randint(-1000, 1000, size=np.random.randint(1, max_size+1)))
        x = count_inversions_naive(xs)
        y = count_inversions(xs)
        if x != y:
            print('test failed', x, y, xs)
            raise
        print('test passed')


def main():
    if DEBUG:
        stress_test(max_size=1000)
    else:
        raw_input()
        xs = map(int, raw_input().split())
        print(count_inversions(xs))


if __name__ == '__main__':
    main()
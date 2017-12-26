# Uses python2


import numpy as np

DEBUG = False


def quicksort(xs):
    def sort(p, r):
        if p < r:
            q1, q2 = partition(xs, p, r)
            sort(p, q1-1)
            sort(q2+1, r)
    sort(0, len(xs)-1)


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


def swap(xs, i, j):
    xs[i], xs[j] = xs[j], xs[i]


def stress_test(max_size):
    while True:
        xs = list(np.random.randint(-10, 10, size=np.random.randint(1, max_size+1)))
        sorted_xs = sorted(xs)
        quicksort(xs)
        if sorted_xs != xs:
            print('test failed')
            raise
        print('test passed')


def main():
    if DEBUG:
        stress_test(max_size=1000)
    else:
        raw_input()
        xs = map(int, raw_input().split())
        quicksort(xs)
        print(' '.join(map(str, xs)))


if __name__ == '__main__':
    main()

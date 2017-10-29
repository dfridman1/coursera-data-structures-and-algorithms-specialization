# Uses python2


def optimal_summands(n):
    k = find_k(n)
    summands = []
    for i in xrange(1, k):
        summands.append(i)
        n -= i
    summands.append(n)
    return summands


def find_k(n):
    lo, hi = 1, n
    while hi-lo > 1:
        mid = (lo + hi) >> 1
        min_value = compute(mid)
        if min_value > n:
            hi = mid-1
        else:
            lo = mid
    min_value = compute(hi)
    return hi if min_value <= n else lo


def compute(n):
    return (n * (n+1)) >> 1


def main():
    n = int(raw_input())
    summands = optimal_summands(n)
    print(len(summands))
    print(' '.join(map(str, summands)))


if __name__ == '__main__':
    main()

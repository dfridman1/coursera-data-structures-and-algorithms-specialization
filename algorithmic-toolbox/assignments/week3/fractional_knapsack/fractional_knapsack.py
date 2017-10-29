# Uses python2


from __future__ import division
import operator as op


def knapsack(values, weights, W):
    pairs = sorted([(v/w, w) for v, w in zip(values, weights)], key=op.itemgetter(0), reverse=True)
    values, weights = zip(*pairs)
    values, weights = list(values), list(weights)
    i = v = 0
    while W > 0 and i < len(values):
        if weights[i] == 0:
            i += 1
            continue
        w = min(W, weights[i])
        v += values[i] * w
        weights[i] -= w
        W -= w
    return v


def main():
    n, W = map(int, raw_input().split())
    vs, ws = [], []
    for _ in xrange(n):
        v, w = map(int, raw_input().split())
        vs.append(v)
        ws.append(w)
    print(knapsack(vs, ws, W))


if __name__ == '__main__':
    main()

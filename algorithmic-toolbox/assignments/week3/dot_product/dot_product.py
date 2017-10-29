#Uses python2


import operator as op


def max_dot_product(xs, ys):
    return sum([x*y for x, y in zip(sorted(xs), sorted(ys))])


def main():
    raw_input()
    xs = map(int, raw_input().split())
    ys = map(int, raw_input().split())
    print(max_dot_product(xs, ys))


if __name__ == '__main__':
    main()

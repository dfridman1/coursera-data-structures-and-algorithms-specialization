# python2


def build_heap(xs):
    swaps = []
    for i in xrange((len(xs)-1)//2, -1, -1):
        swaps.extend(sift_down(xs, i))
    return swaps


def sift_down(xs, i):
    swaps = []
    while True:
        min_i = i
        left_i, right_i = 2*i+1, 2*i+2
        if left_i < len(xs) and xs[left_i] < xs[min_i]:
            min_i = left_i
        if right_i < len(xs) and xs[right_i] < xs[min_i]:
            min_i = right_i
        if min_i != i:
            swaps.append((i, min_i))
            xs[i], xs[min_i] = xs[min_i], xs[i]
            i = min_i
        else:
            break
    return swaps


def get_data():
    raw_input()
    return map(int, raw_input().split())


def main():
    xs = get_data()
    swaps = build_heap(xs)
    print(len(swaps))
    for x, y in swaps:
        print('{} {}'.format(x, y))


if __name__ == '__main__':
  main()

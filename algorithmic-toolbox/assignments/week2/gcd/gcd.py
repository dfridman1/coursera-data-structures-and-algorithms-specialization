# Uses python2


import numpy as np

DEBUG = False


def gcd(m, n):
    return m if n == 0 else gcd(n, m % n)


def gcd_naive(m, n):
    d = min(m, n)
    while not (m % d == 0 and n % d == 0):
        d -= 1
    return d


def stress_test(max_n):
    assert max_n > 0
    gen = lambda: np.random.randint(1, max_n+1)
    while True:
        m, n = gen(), gen()
        x, y = gcd(m, n), gcd_naive(m, n)
        if x != y:
            print('test failed', x, y)
            raise
        print('test passed')


def main():
    if DEBUG:
        stress_test(max_n=1000)
    else:
        m, n = map(int, raw_input().split())
        print(gcd(m, n))



if __name__ == '__main__':
    main()

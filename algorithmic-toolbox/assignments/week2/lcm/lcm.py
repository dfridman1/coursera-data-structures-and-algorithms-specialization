# Uses python2


def gcd(m, n):
    return m if n == 0 else gcd(n, m % n)


def lcm(m, n):
    return (m * n) // gcd(m, n)


def main():
    m, n = map(int, raw_input().split())
    print(lcm(m, n))


if __name__ == '__main__':
    main()

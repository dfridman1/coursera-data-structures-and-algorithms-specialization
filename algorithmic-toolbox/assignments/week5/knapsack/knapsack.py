# Uses python2


def knapsack(W, ws):
    n = len(ws)
    dp = [[False for _ in xrange(W+1)] for _ in xrange(n+1)]
    dp[0][0] = True
    for i in xrange(1, n+1):
        w = ws[i-1]
        for j in xrange(W+1):
            dp[i][j] |= dp[i-1][j]
            if j >= w:
                dp[i][j] |= dp[i-1][j-w]
    i = W
    while i >= 0 and not dp[n][i]:
        i -= 1
    return i


def main():
    W, _ = map(int, raw_input().split())
    ws = map(int, raw_input().split())
    print(knapsack(W, ws))


if __name__ == '__main__':
    main()
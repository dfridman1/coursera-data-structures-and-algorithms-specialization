#Uses python2


def lcm3(s1, s2, s3):
    l, m, n = len(s1), len(s2), len(s3)
    dp = [[[0 for _ in xrange(n+1)] for _ in xrange(m+1)] for _ in xrange(l+1)]
    for i in xrange(1, l+1):
        for j in xrange(1, m+1):
            for k in xrange(1, n+1):
                if s1[i-1] == s2[j-1] and s1[i-1] == s3[k-1]:
                    dp[i][j][k] = 1 + dp[i-1][j-1][k-1]
                else:
                    dp[i][j][k] = max(dp[i-1][j-1][k],
                                      dp[i-1][j][k-1],
                                      dp[i-1][j][k],
                                      dp[i][j-1][k],
                                      dp[i][j-1][k-1],
                                      dp[i][j][k-1])
    return dp[l][m][n]


def _parse_input():
    raw_input()
    s1 = raw_input().split()
    raw_input()
    s2 = raw_input().split()
    raw_input()
    s3 = raw_input().split()
    return s1, s2, s3


def main():
    s1, s2, s3 = _parse_input()
    print(lcm3(s1, s2, s3))


if __name__ == '__main__':
    main()

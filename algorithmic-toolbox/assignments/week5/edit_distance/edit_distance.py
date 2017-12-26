# Uses python2


def edit_distance(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0 for _ in xrange(n+1)] for _ in xrange(m+1)]
    for i in xrange(m+1):
        dp[i][0] = i
    for i in xrange(n+1):
        dp[0][i] = i
    for i in xrange(1, m+1):
        for j in xrange(1, n+1):
            dp[i][j] = min(1 + dp[i-1][j],  # D
                           1 + dp[i][j-1],  # I
                           dp[i-1][j-1] + (s1[i-1] != s2[j-1]))  # X?
    return dp[m][n]


def edit_distance2(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0 for _ in xrange(n+1)] for _ in xrange(m+1)]
    actions = [[None for _ in xrange(n+1)] for _ in xrange(m+1)]
    for i in xrange(m+1):
        dp[i][0] = i
        actions[i][0] = 'D'
    for i in xrange(n+1):
        dp[0][i] = i
        actions[0][i] = 'I'
    for i in xrange(1, m+1):
        for j in xrange(1, n+1):
            delete = 1 + dp[i-1][j]
            insert = 1 + dp[i][j-1]
            maybe_change = dp[i-1][j-1] + (s1[i-1] != s2[j-1])
            min_e = min(delete, insert, maybe_change)
            dp[i][j] = min_e
            if min_e == insert:
                actions[i][j] = 'I'
            elif min_e == delete:
                actions[i][j] = 'D'
            elif s1[i-1] == s2[j-1]:
                actions[i][j] = 'M'
            else:
                actions[i][j] = 'X'
    cigar = []
    i, j = m, n
    while i > 0 or j > 0:
        a = actions[i][j]
        cigar.append(a)
        if a in ['M', 'X']:
            i -= 1
            j -= 1
        elif a == 'D':
            i -= 1
        else:
            j -= 1

    return ''.join(reversed(cigar))


def display(s1, s2, cigar):
    x, y = [], []
    i = j = 0
    for c in cigar:
        if c in ['M', 'X']:
            x.append(s1[i])
            y.append(s2[j])
            i += 1
            j += 1
        elif c == 'D':
            x.append(s1[i])
            y.append('-')
            i += 1
        else:
            x.append('-')
            y.append(s2[j])
            j += 1
    return x, y


def main():
    s1, s2 = raw_input(), raw_input()
    cigar = edit_distance2(s1, s2)
    x, y = display(s1, s2, cigar)
    print(cigar)
    print(x)
    print(y)


if __name__ == "__main__":
    main()

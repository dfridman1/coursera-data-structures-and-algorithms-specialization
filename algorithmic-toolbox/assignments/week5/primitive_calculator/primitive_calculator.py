# Uses python2


def primitive_calculator(n):
    dp = [0] * (n+1)
    dp_action = [0] * (n+1)
    for i in xrange(1, n+1):
        t = dp[i-1]
        action = 1
        if i % 2 == 0 and dp[i//2] < t:
            t = dp[i//2]
            action = 2
        if i % 3 == 0 and dp[i//3] < t:
            t = dp[i//3]
            action = 3
        dp[i] = 1 + t
        dp_action[i] = action
    sequence = []
    while n > 0:
        sequence.append(n)
        a = dp_action[n]
        if a == 1:
            n -= 1
        elif a == 2:
            n //= 2
        else:
            n //= 3
    sequence = list(reversed(sequence))
    return sequence


def main():
    n = int(raw_input())
    sequence = primitive_calculator(n)
    print(len(sequence)-1)
    print(' '.join(map(str, sequence)))


if __name__ == '__main__':
    main()

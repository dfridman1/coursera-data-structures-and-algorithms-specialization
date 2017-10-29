# Uses python2



def count_change(m, coins):
    coins = sorted(coins)
    cnt = 0
    while m > 0:
        coin = coins.pop()
        while m - coin >= 0:
            m -= coin
            cnt += 1
    return cnt


def main():
    m = int(raw_input())
    coins = [1, 5, 10]
    print(count_change(m, coins))


if __name__ == '__main__':
    main()
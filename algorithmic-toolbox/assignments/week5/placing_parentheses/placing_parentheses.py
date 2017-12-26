# Uses python2

import operator as op


def maximize_value(nums, ops):
    assert len(nums) == len(ops) + 1
    n = len(nums)
    dp_max = [[float('-inf') for _ in xrange(n)] for _ in xrange(n)]
    dp_min = [[float('inf') for _ in xrange(n)] for _ in xrange(n)]
    for i in xrange(n):
        dp_max[i][i] = dp_min[i][i] = nums[i]
    for l in xrange(2, n+1):
        for i in xrange(n-l+1):
            j = i + l - 1
            for k in xrange(i, j):
                op = ops[k]
                options = [
                    op(dp_max[i][k], dp_max[k+1][j]),
                    op(dp_max[i][k], dp_min[k+1][j]),
                    op(dp_min[i][k], dp_max[k+1][j]),
                    op(dp_min[i][k], dp_min[k+1][j])
                ]
                dp_max[i][j] = max(dp_max[i][j], max(options))
                dp_min[i][j] = min(dp_min[i][j], min(options))
    return dp_max[0][n-1]


def get_op(op_name):
    mapping = {
        '+': op.add,
        '-': op.sub,
        '*': op.mul
    }
    return mapping[op_name]


def main():
    s = raw_input()
    nums = map(int, s[::2])
    ops = map(get_op, s[1::2])
    print(maximize_value(nums, ops))


if __name__ == '__main__':
    main()
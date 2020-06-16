from math import log, floor


def preprocess_rmq(n, a):
    t = floor(log(n, 2))
    rmq = [[0 for i in range(n)] for j in range(t + 1)]
    for i in range(n):
        rmq[0][i] = a[i]
    for k in range(1, t + 1):
        for i in range(n):
            if (i + 2 ** (k - 1)) < n:
                rmq[k][i] = min(rmq[k - 1][i], rmq[k - 1][i + 2 ** (k - 1)])
            else:
                rmq[k][i] = rmq[k - 1][i]
    return rmq


def min_rmq(rmq, n, l, r):
    ans = float('inf')
    max_t = floor(log(n, 2))
    for t in range(max_t, -1, -1):
        if (2 ** t) <= (r - l):
            ans = min(ans, rmq[t][l])
            l = l + 2 ** t
    return ans


def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    rmq = preprocess_rmq(n, a)
    for i in range(q):
        l, r = map(int, input().split())
        print(min_rmq(rmq, n, l, r + 1))
    pass


if __name__ == '__main__':
    main()

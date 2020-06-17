import bisect
from math import sqrt, floor, log


def preprocess_rmq(n, a):
    t = floor(log(n, 2))
    rmq = [[0 for i in range(n)] for j in range(t + 1)]
    for i in range(n):
        rmq[0][i] = a[i]
    for k in range(1, t + 1):
        for i in range(n):
            if (i + 2 ** (k - 1)) < n:
                rmq[k][i] = max(rmq[k - 1][i], rmq[k - 1][i + 2 ** (k - 1)])
            else:
                rmq[k][i] = rmq[k - 1][i]
    return rmq


def max_rmq(rmq, n, l, r):
    ans = float('-inf')
    max_t = floor(log(n, 2))
    for t in range(max_t, -1, -1):
        if (2 ** t) <= (r - l):
            ans = max(ans, rmq[t][l])
            l = l + 2 ** t
    return ans


def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    changes = []
    t = int(sqrt(n))
    rmq = preprocess_rmq(n, a)
    for i in range(q):
        if i % t == 0:
            changes.clear()
            rmq = preprocess_rmq(n, a)
        row = list(map(int, input().split()))
        if row[0] == 1:
            l = row[1]
            r = row[2]
            index = bisect.bisect(changes, l)
            ans = float('-inf')
            while index < len(changes) and changes[index] <= r:
                ans = max(ans, max_rmq(rmq, n, l, changes[index]), a[changes[index]])
                l = changes[index] + 1
                index += 1
            ans = max(ans, max_rmq(rmq, n, l, r + 1))
            print(ans)
        elif row[0] == 2:
            idx = row[1]
            nv = row[2]
            bisect.insort(changes, idx)
            a[idx] = nv
    pass


if __name__ == '__main__':
    main()
import bisect
from math import sqrt

# bisect.insort()
def get_ps(n, a):
    ps = [0 for i in range(n + 1)]
    for i in range(1, n + 1):
        ps[i] = ps[i - 1] + a[i - 1]
    return ps


def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    # ps = get_ps(n, a)
    changes = []
    t = int(sqrt(n))
    for i in range(q):
        if i % t == 0:
            changes.clear()
            ps = get_ps(n, a)
        row = list(map(int, input().split()))
        if row[0] == 1:
            l = row[1]
            r = row[2]
            index = bisect.bisect(changes, (l, float('-inf')))
            ans = ps[r + 1] - ps[l]
            while index < len(changes) and changes[index][0] <= r:
                ans += changes[index][1]
                index += 1
            print(ans)
        elif row[0] == 2:
            idx = row[1]
            nv = row[2]
            bisect.insort(changes, (idx, nv - a[idx]))
            a[idx] = nv
    pass


if __name__ == '__main__':
    main()
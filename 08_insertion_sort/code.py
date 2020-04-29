import sys
sys.setrecursionlimit(2000)


def sort(a, i):
    if i > 1:
        sort(a, i - 1)
    k = i - 1
    while k > 0 and a[k] < a[k - 1]:
        x = a[k]
        a[k] = a[k - 1]
        a[k - 1] = x
        k = k - 1
    pass


n = int(input())
b = [int(x) for x in input().split()]
sort(b, n)
print(' '.join(str(x) for x in b))

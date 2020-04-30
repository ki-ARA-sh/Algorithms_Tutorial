import sys
sys.setrecursionlimit(10**6)


def fn(i):
    if i == 0:
        return 5
    tmp = fn(i - 1)
    if i % 2 == 0:
        return tmp - 21
    else:
        return tmp * tmp


n = int(input())
result = fn(n)
print(result)

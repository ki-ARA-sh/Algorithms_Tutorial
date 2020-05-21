

def f(a, n, m, i, j):
    if (i == n - 1) and (j == m - 1):
        return a[i][j], ""
    elif i == n - 1:
        p, q = f(a, n, m, i, j + 1)
        return a[i][j] + p, "R" + q
    elif j == m - 1:
        p, q = f(a, n, m, i + 1, j)
        return a[i][j] + p, "U" + q
    else:
        p1, q1 = f(a, n, m, i, j + 1)
        p2, q2 = f(a, n, m, i + 1, j)
        if p1 > p2:
            p = p1
            q = "R" + q1
        else:
            p = p2
            q = "U" + q2
        return a[i][j] + p, q


def main():
    n, m = map(int, input().split())
    a = list()
    for i in range(n):
        a.insert(0, list(map(int, input().split())))
    p, q = f(a, n, m, 0, 0)
    print(p)
    print(q)


if __name__ == '__main__':
    main()


def f(m, n, i, j):
    if (i == n - 1) or (j == m - 1):
        return 1
    return f(m, n, i, j + 1) + f(m, n, i + 1, j)


print(f(4, 4, 0, 0))

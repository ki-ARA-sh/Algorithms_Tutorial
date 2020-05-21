def f(a, n, m):
    path = [[0 for i in range(m)] for j in range(n)]
    path[0][0] = a[0][0]
    for i in range(1, m):
        path[0][i] = path[0][i - 1] + a[0][i]
    for i in range(1, n - 1):
        for j in range(m):
            line = [0 for k in range(m)]
            line[j] = path[i - 1][j] + a[i][j]
            path[i][j] = line[j]
            for k in range(j - 1, -1, -1):
                line[k] = line[k + 1] - path[i - 1][k + 1] + path[i - 1][k] + a[i][k]
                path[i][j] = min(path[i][j], line[k])
            for k in range(j + 1, m):
                line[k] = line[k - 1] - path[i - 1][k - 1] + path[i - 1][k] + a[i][k]
                path[i][j] = min(path[i][j], line[k])
    # path[n - 1][m - 1] = path[n - 2][m - 1] + a[n - 1][m - 1]
    result = prev = path[n - 2][m - 1] + a[n - 1][m - 1]
    for i in range(m - 2, -1, -1):
        # prev = path[n - 1][i + 1] - path[n - 2][i + 1] + path[n - 2][i] + a[n - 1][i]
        prev = prev - path[n - 2][i + 1] + path[n - 2][i] + a[n - 1][i]
        result = min(result, prev)
    return result


def main():
    n, m = map(int, input().split())
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))
    print(f(a, n, m))


if __name__ == '__main__':
    main()

def submatrix_sum(x1, y1, x2, y2, ps):
    result = 0
    if x1 <= x2 and y1 <= y2:
        result = ps[x2][y2]
        if x1 > 0:
            result = result - ps[x1 - 1][y2]
        if y1 > 0:
            result = result - ps[x2][y1 - 1]
        if x1 > 0 and y1 > 0:
            result = result + ps[x1 - 1][y1 - 1]
    return result


def main():
    n, m, k = map(int, input().split())
    ps = [[0 for j in range(m)] for i in range(n)]
    row = list(map(int, input().split()))
    ps[0][0] = row[0]
    for i in range(1, m):
        ps[0][i] = ps[0][i - 1] + row[i]
    for i in range(1, n):
        row = list(map(int, input().split()))
        ps[i][0] = ps[i - 1][0] + row[0]
        for j in range(1, m):
            ps[i][j] = ps[i - 1][j] + ps[i][j - 1] + row[j] - ps[i - 1][j - 1]
    base = m * n - submatrix_sum(0, 0, n - 1, m - 1, ps)
    result = 0
    psk = [[0 for i in range(m - k + 1)] for j in range(n - k + 1)]
    for i in range(n - k + 1):
        for j in range(m - k + 1):
            psk[i][j] = submatrix_sum(i, j, i + k - 1, j + k - 1, ps)
    for i in range(n - k + 1):
        for j in range(m - k + 1):
            for p in range(i, n - k + 1):
                for q in range(j, m - k + 1):
                    result = max(result, base + psk[i][j] + psk[p][q] - submatrix_sum(p, q, i + k - 1, j + k - 1, ps))
    print(result)


if __name__ == '__main__':
    main()
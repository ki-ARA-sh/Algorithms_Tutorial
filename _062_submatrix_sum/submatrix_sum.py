
def submatrix_sum(x1, y1, x2, y2, ps):
    result = ps[x2][y2]
    if x1 > 0:
        result = result - ps[x1 - 1][y2]
    if y1 > 0:
        result = result - ps[x2][y1 - 1]
    if x1 > 0 and y1 > 0:
        result = result + ps[x1 - 1][y1 - 1]
    return result



def main():
    n, q = map(int, input().split())
    ps = [[0 for i in range(n)] for i in range(n)]
    row = list(map(int, input().split()))
    ps[0][0] = row[0]
    for i in range(1, n):
        ps[0][i] = ps[0][i - 1] + row[i]
    for i in range(1, n):
        row = list(map(int, input().split()))
        ps[i][0] = ps[i - 1][0] + row[0]
        for j in range(1, n):
            ps[i][j] = ps[i - 1][j] + ps[i][j - 1] + row[j] - ps[i - 1][j - 1]
    for i in range(q):
        x1, y1, x2, y2 = map(int, input().split())
        print(submatrix_sum(x1, y1, x2, y2, ps))
    pass


if __name__ == '__main__':
    main()

def f(a, n, m, i, j, nxt='D'):
    p1 = p2 = p3 = float('inf')
    if i == 0 and j == 0:
        return a[0][0]
    if (nxt != 'R') and (j != m - 1):
        p1 = f(a, n, m, i, j + 1, 'L')
    if (nxt != 'L') and (j != 0):
        p2 = f(a, n, m, i, j - 1, 'R')
    if i != 0:
        p3 = f(a, n, m, i - 1, j)
    return min(p1, p2, p3) + a[i][j]
    

def main():
    n, m = map(int, input().split())
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))
    print(f(a, n, m, n - 1, m - 1))


if __name__ == '__main__':
    main()

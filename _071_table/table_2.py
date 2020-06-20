import sys
sys.setrecursionlimit(10**6)


def dfs(r, c, a, n, mark):
    mark[r][c] = True
    smallers = 0
    largers = 0
    for i in range(max(0, r - 1), min(n, r + 2)):
        for j in range(max(0, c - 1), min(n, c + 2)):
            if (not mark[i][j]) and (a[i][j] == a[r][c]):
                smallers1, largers1 = dfs(i, j, a, n, mark)
                smallers = smallers + smallers1
                largers = largers + largers1
            if a[i][j] > a[r][c]:
                largers = largers + 1
            elif a[i][j] < a[r][c]:
                smallers = smallers + 1
    return smallers, largers


def main():
    n = int(input())
    a = [None] * n
    for i in range(n):
        a[i] = list(map(int, input().split()))
    mark = [[False for i in range(n)] for j in range(n)]
    summit_num = 0
    valley_num = 0
    for i in range(n):
        for j in range(n):
            if not mark[i][j]:
                border_s, border_l = dfs(i, j, a, n, mark)
                if border_s > 0 and border_l == 0:
                    summit_num += 1
                if border_s == 0 and border_l > 0:
                    valley_num += 1
    print(str(summit_num) + ' ' + str(valley_num))


if __name__ == '__main__':
    main()


import sys
sys.setrecursionlimit(10**6)


def dfs(r, c, a, n, mark):
    mark[r][c] = True
    result = []
    for i in range(max(0, r - 1), min(n, r + 2)):
        for j in range(max(0, c - 1), min(n, c + 2)):
            if (not mark[i][j]) and (a[i][j] == a[r][c]):
                border = dfs(i, j, a, n, mark)
                for cell in border:
                    if cell not in result:
                        result = result + [cell]
            if a[i][j] != a[r][c]:
                if (i, j) not in result:
                    result = result + [(i, j)]
    return result


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
                border = dfs(i, j, a, n, mark)
                is_summit = True
                is_valley = True
                for cell in border:
                    if a[i][j] > a[cell[0]][cell[1]]:
                        is_valley = False
                    elif a[i][j] < a[cell[0]][cell[1]]:
                        is_summit = False
                if is_summit:
                    summit_num += 1
                elif is_valley:
                    valley_num += 1
    print(str(summit_num) + ' ' + str(valley_num))


if __name__ == '__main__':
    main()


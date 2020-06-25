import sys
sys.setrecursionlimit(10**6)


def dfs(r, c, L, a, n, mark):
    mark[r][c] = True
    L.append((r, c))
    for i in range(max(0, r - 1), min(n, r + 2)):
        for j in range(max(0, c - 1), min(n, c + 2)):
            if i != r or j != c:
                if (not mark[i][j]) and (a[i][j] == a[r][c]):
                    dfs(i, j, L, a, n, mark)
    pass


def get_border(component, n):
    result = []
    for vertex in component:
        r = vertex[0]
        c = vertex[1]
        for i in range(max(0, r - 1), min(n, r + 2)):
            for j in range(max(0, c - 1), min(n, c + 2)):
                if i != r or j != c:
                    if ((i, j) not in component) and ((i, j) not in result):
                        result = result + [(i, j)]
    return result


def main():
    n = int(input())
    a = [None] * n
    for i in range(n):
        a[i] = list(map(int, input().split()))
    mark = [[False for i in range(n)] for j in range(n)]
    result = [0, 0]
    for i in range(n):
        for j in range(n):
            if not mark[i][j]:
                component = []
                dfs(i, j, component, a, n, mark)
                border = get_border(component, n)
                is_greater = 0
                is_less = 0
                for cell in border:
                    if a[i][j] > a[cell[0]][cell[1]]:
                        is_greater += 1
                    elif a[i][j] < a[cell[0]][cell[1]]:
                        is_less += 1
                if is_greater > 0 and is_less == 0:
                    result[0] = result[0] + 1
                elif is_greater == 0 and is_less > 0:
                    result[1] = result[1] + 1
    if result == [0, 0]:
        result = [1, 1]
    print(' '.join(list(map(str, result))))


if __name__ == '__main__':
    main()


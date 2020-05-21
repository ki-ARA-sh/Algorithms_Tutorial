

def f(a, n, m):
    dp = [[0 for i in range(m)] for j in range(n)]
    dp[0][0] = a[0][0]
    way = [["" for i in range(m)] for j in range(n)]
    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                dp[i][j] = a[i][j]
            elif i == 0:
                dp[i][j] = dp[i][j - 1] + a[i][j]
                way[i][j] = way[i][j - 1] + "R"
            elif j == 0:
                dp[i][j] = dp[i - 1][j] + a[i][j]
                way[i][j] = way[i - 1][j] + "U"
            else:
                if dp[i - 1][j] > dp[i][j - 1]:
                    dp[i][j] = dp[i - 1][j] + a[i][j]
                    way[i][j] = way[i - 1][j] + "U"
                else:
                    dp[i][j] = dp[i][j - 1] + a[i][j]
                    way[i][j] = way[i][j - 1] + "R"
    return dp[n - 1][m - 1], way[n - 1][m - 1]


def main():
    n, m = map(int, input().split())
    a = list()
    for i in range(n):
        a.insert(0, list(map(int, input().split())))
    p, q = f(a, n, m)
    print(p)
    print(q)


if __name__ == '__main__':
    main()

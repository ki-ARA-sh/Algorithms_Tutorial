
def f(a):
    if len(a) < 3:
        return 0
    return min(a[0] * a[1] * a[-1] + f(a[1:]), a[0] * a[1] * a[2] + f([a[0]] + a[2:]))


def g(n, a):
    dp = [[0 for i in range(n + 1)] for j in range(n + 1)]
    for r in range(2, n + 1):
        for l in range(r - 1, 0, -1):
            dp[l][r] = float("inf")
            for i in range(l, r):
                dp[l][r] = min(dp[l][r], dp[l][i] + dp[i + 1][r] + a[l - 1] * a[i] * a[r])
    return dp[1][n]


def main():
    n = int(input())
    a = list(map(int, input().split()))
    # print(f(a))
    print(g(n, a))


if __name__ == '__main__':
    main()
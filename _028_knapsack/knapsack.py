from unittest import TestCase


def knapsack_recursive(w, v, n, s):
    if n == 0:
        return 0
    a = knapsack_recursive(w, v, n - 1, s)
    b = float('-inf')
    if w[n - 1] <= s:
        b = knapsack_recursive(w, v, n - 1, s - w[n - 1]) + v[n - 1]
    return max(a, b)


def knapsack_dp(w, v, n, s):
    dp = [[0 for i in range(n)] for j in range(s)]
    for i in range(1, n):
        for j in range(s, -1, -1):
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w[i]] + v[i])
    return dp[n][s]


def main():
    n = int(input())
    w = list(map(int, input().split()))
    v = list(map(int, input().split()))
    s = int(input())
    print(knapsack_recursive(w, v, n, s))

if __name__ == '__main__':
    main()


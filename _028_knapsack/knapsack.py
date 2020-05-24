
def knapsack_recursive(w, v, n, s):
    if n == 0:
        return 0
    a = knapsack_recursive(w, v, n - 1, s)
    b = float('-inf')
    if w[n - 1] <= s:
        b = knapsack_recursive(w, v, n - 1, s - w[n - 1]) + v[n - 1]
    return max(a, b)


def knapsack_dp(w, v, n, s):
    dp = [[0 for i in range(s + 1)] for j in range(n + 1)]
    par = [[0 for i in range(s + 1)] for j in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(s, -1, -1):
            if (w[i - 1] <= j) and (dp[i - 1][j - w[i - 1]] + v[i - 1] > dp[i - 1][j]):
                dp[i][j] = dp[i - 1][j - w[i - 1]] + v[i - 1]
                par[i][j] = 1
            else:
                dp[i][j] = dp[i - 1][j]
                par[i][j] = 0
    # current_weight = s - 1
    # for i in range(n - 1, -1, -1):
    #     if par[i][current_weight] == 1:
    #         print('take {}'.format(i + 1))
    #         current_weight = current_weight - w[i]
    return dp[n][s]


def knapsack_dp_optimized_memory(w, v, n, s):
    dp = [[0 for i in range(s + 1)] for j in range(2)]
    for i in range(1, n + 1):
        for j in range(s, -1, -1):
            if (w[i - 1] <= j) and (dp[(i - 1) % 2][j - w[i - 1]] + v[i - 1] > dp[(i - 1) % 2][j]):
                dp[i % 2][j] = dp[(i - 1) % 2][j - w[i - 1]] + v[i - 1]
            else:
                dp[i % 2][j] = dp[(i - 1) % 2][j]
    return dp[n % 2][s]


def knapsack_exact_recursive(w, n, s):
    if s == 0:
        return 1
    elif len(w) == 0:
        return 0
    return knapsack_exact_recursive(w[1:], n - 1, s - w[0]) + knapsack_exact_recursive(w[1:], n - 1, s)


def knapsack_exact_dp(w, n, s):
    dp = [[0 for i in range(s + 1)] for j in range(n + 1)]
    dp[0][0] = 1
    for i in range(1, n + 1):
        for j in range(s + 1):
            dp[i][j] = dp[i - 1][j]
            if j >= w[i - 1]:
                dp[i][j] = dp[i][j] + dp[i - 1][j - w[i - 1]]
    return dp[n][s]


def knapsack_inf_recursive(w, v, n, s):
    if n == 0:
        return 0
    ans = float("-inf")
    for i in range(s // w[0] + 1):
        ans = max(ans, knapsack_inf_recursive(w[1:], v[1:], n - 1, s - i * w[0]) + i * v[0])
    return ans


def knapsack_inf_dp(w, v, n, s):
    pass


def main():
    n = int(input())
    w = list(map(int, input().split()))
    v = list(map(int, input().split()))
    s = int(input())
    print(knapsack_recursive(w, v, n, s))


if __name__ == '__main__':
    main()

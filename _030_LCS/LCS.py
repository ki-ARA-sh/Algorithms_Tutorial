
def lcs(p, q):
    n = len(p)
    m = len(q)
    dp = [[0 for i in range(m + 1)] for j in range(2)]
    updates = [["" for i in range(m + 1)] for j in range(2)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            dp[i % 2][j] = max(dp[(i - 1) % 2][j], dp[(i % 2)][j - 1])
            if p[i - 1] == q[j - 1]:
                dp[i % 2][j] = max(dp[i % 2][j], dp[(i - 1) % 2][j - 1] + 1)
            if dp[i % 2][j] == dp[(i - 1) % 2][j]:
                updates[i % 2][j] = updates[(i - 1) % 2][j]
            elif dp[i % 2][j] == dp[(i % 2)][j - 1]:
                updates[i % 2][j] = updates[(i % 2)][j - 1]
            else:
                updates[i % 2][j] = updates[(i - 1) % 2][j - 1] + p[i - 1]
    return dp[n % 2][m], updates[n % 2][m]


def main():
    p = input()
    q = input()
    s, t = lcs(p, q)
    print(s)
    print(t)


if __name__ == '__main__':
    main()
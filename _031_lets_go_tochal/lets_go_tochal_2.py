n = int(input())
A = list(map(int, input().split(" ")))

dp = [[0] * (n + 1) for i in range(n + 1)]

for i in range(0, n + 1):
    dp[i][i] = 1

mod = 1000 * 1000 * 1000 + 7

for len in range(1, n + 1):
    for l in range(n-len + 1):
        r = l + len
        if r - l == 1:
            dp[l][r] = 1
        else:
            dp[l][r] = dp[l][r - 1]
            if A[l] != A[r - 1]:
                continue
            dp[l][r] += 1
            for k in range(l + 1, r - 1):
                if A[k] >= A[l]:
                    dp[l][r] += dp[k][r - 1]
                    dp[l][r] %= mod
ans = 0
for l in range(0, n):
    ans += dp[l][n]
    ans %= mod
print (ans)

def all_one_none(w, n, s):
    neg_inf = float("-inf")
    dp = [[0 for i in range(s + 1)] for j in range(n + 1)]
    seq = [["" for i in range(s + 1)] for j in range(n + 1)]
    for i in range(1, n + 1):
        sum_w_i = sum(w[i - 1])
        size_w_i = len(w[i - 1])
        for j in range(s, -1, -1):
            one_picked = neg_inf
            one_picked_seq = ""
            all_picked = neg_inf
            for k in range(size_w_i):
                one_picked_temp = neg_inf
                if j >= w[i - 1][k]:
                    one_picked_temp = dp[i - 1][j - w[i - 1][k]] + 1
                if one_picked_temp > one_picked:
                    one_picked = one_picked_temp
                    one_picked_seq = seq[i - 1][j - w[i - 1][k]]
            if j >= sum_w_i:
                all_picked = dp[i - 1][j - sum_w_i] + size_w_i
            none_picked = dp[i - 1][j]
            dp[i][j] = max(one_picked, all_picked, none_picked)
            if one_picked == dp[i][j]:
                seq[i][j] = one_picked_seq + "1"
            elif none_picked == dp[i][j]:
                seq[i][j] = seq[i - 1][j] + "0"
            elif all_picked == dp[i][j]:
                seq[i][j] = seq[i - 1][j - sum_w_i] + "2"
    return dp[n][s], seq[n][s]


def main():
    n, s = map(int, input().split())
    w = []
    for i in range(n):
        a = list(map(int, input().split()))
        w.append(a[1:])
    p, q = all_one_none(w, n ,s)
    print(p)
    print(q)


if __name__ == '__main__':
    main()

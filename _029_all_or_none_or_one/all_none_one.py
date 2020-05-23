
def all_one_none(w, n, s):
    neg_inf = float("-inf")
    dp = [[0 for i in range(s + 1)] for j in range(n + 1)]
    par = [[-1 for i in range(s + 1)] for j in range(n + 1)]
    one_is_picked = [[False for i in range(s + 1)] for j in range(n + 1)]
    for i in range(1, n + 1):
        sum_w_i = sum(w[i - 1])
        size_w_i = len(w[i - 1])
        for j in range(s, -1, -1):
            one_picked = neg_inf
            which_one_picked = -1
            all_picked = neg_inf
            for k in range(size_w_i):
                one_picked_temp = neg_inf
                if j >= w[i - 1][k]:
                    one_picked_temp = dp[i - 1][j - w[i - 1][k]] + 1
                    if one_picked_temp > one_picked:
                        one_picked = one_picked_temp
                        which_one_picked = k
                else:
                    break
            if j >= sum_w_i:
                all_picked = dp[i - 1][j - sum_w_i] + size_w_i
            none_picked = dp[i - 1][j]
            dp[i][j] = max(one_picked, all_picked, none_picked)
            if one_picked == dp[i][j]:
                par[i][j] = which_one_picked
            elif none_picked == dp[i][j]:
                par[i][j] = '0'
            elif all_picked == dp[i][j]:
                par[i][j] = '2'
    purchase = ""
    current_money = s
    for i in range(n, 0, -1):
        if isinstance(par[i][current_money], str):
            purchase = purchase + par[i][current_money]
            if par[i][current_money] == '2':
                current_money = current_money - sum(w[i - 1])
        else:
            purchase = purchase + "1"
            current_money = current_money - w[i - 1][par[i][current_money]]
    return dp[n][s], purchase[::-1]


def main():
    n, s = map(int, input().split())
    w = []
    for i in range(n):
        a = list(map(int, input().split()))
        if len(a) > 1:
            w.append(sorted(a[1:]))
        else:
            w.append([])
    p, q = all_one_none(w, n, s)
    print(p)
    print(q)


if __name__ == '__main__':
    main()

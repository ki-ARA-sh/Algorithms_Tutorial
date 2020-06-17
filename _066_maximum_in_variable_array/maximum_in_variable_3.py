import math


def preprocess_rmq(n, a):
    t = math.floor(math.log(n, 2))
    rmq = [[0 for i in range(n)] for j in range(t + 1)]
    for i in range(n):
        rmq[0][i] = a[i]
    for k in range(1, t + 1):
        for i in range(n):
            if (i + 2 ** (k - 1)) < n:
                rmq[k][i] = max(rmq[k - 1][i], rmq[k - 1][i + 2 ** (k - 1)])
            else:
                rmq[k][i] = rmq[k - 1][i]
    return rmq


def max_rmq(rmq, n, l, r):
    ans = float('-inf')
    max_t = math.floor(math.log(n, 2))
    for t in range(max_t, -1, -1):
        if (2 ** t) <= (r - l):
            ans = max(ans, rmq[t][l])
            l = l + 2 ** t
    return ans


MAX_N = 100010
sum = [0] * MAX_N

n,q = list(map(int ,input().split()))
T = int(math.sqrt(n))
a = list(map(int, input().split()))

for i in range(n):
    sum[int(i/T)] += a[i] # sum[x] = a[x*T] + ... + a[(x+1)*T-1]

for i in range(q):
    inp = list(map(int ,input().split()))
    queryType = inp[0]
    if queryType == 1:
        L = inp[1]
        R = inp[2]
        result = 0
        cur = L
        # result = max : a[L] ... , a[k-1] , mx[k/T], mx[k/T+1], ... mx[(k+s)/T], a[k+s], ..., a[R-1]
        while cur <= R :
            if (int(cur / T) * T == cur and cur + T <= R):
                result += sum[int(cur / T)];
                cur += T;
            else :
                result += a[cur];
                cur += 1;
        print(result)
    else:
        idx = inp[1]
        nv = inp[2]
        sum[int(idx/T)] -= a[idx]
        a[idx] = nv
        sum[int(idx/T)] += a[idx];



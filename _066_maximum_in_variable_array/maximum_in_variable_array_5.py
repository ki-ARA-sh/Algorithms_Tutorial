import math

n,q = list(map(int, input().split()))
T = int(math.sqrt(n))
a = list(map(int, input().split()))

MAX_N = math.ceil(n / T)
maximums = [float('-inf')] * MAX_N
for i in range(MAX_N):
    maximums[i] = max(a[(i * T):(min(n, (i + 1) * T))])
    # maximums[int(i / T)] = max(a[i], maximums[int(i / T)]) # sum[x] = a[x*T] + ... + a[(x+1)*T-1]


for i in range(q):
    inp = list(map(int, input().split()))
    queryType = inp[0]
    if queryType == 1:
        L = inp[1]
        R = inp[2]
        result = float('-inf')
        try:
            result = max(result, max(maximums[(math.floor(L / T) + 1):math.floor(R / T)]))
        except:
            pass
        try:
            result = max(result, max(a[L:T * (1 + math.floor(L / T))]))
        except:
            pass
        try:
            result = max(result, max(a[T * math.floor(R / T):(R + 1)]))
        except:
            pass
        print(result)
    else:
        idx = inp[1]
        nv = inp[2]
        a[idx] = nv
        index = idx // T
        maximums[index] = max(a[(T * index):(min(n, T * (index + 1)))]);



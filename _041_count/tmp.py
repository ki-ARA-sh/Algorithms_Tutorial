
n = 10
a = [i + 1 for i in range(n)]
# ps = [0 for i in range(n)]
# ps = [a[i] + ps[i - 1] for i in range(10)]
# ps = [sum(a[:i]) for i in range(1, n + 1)]
ps = [a[0]]
for j in range(1, n):
    ps.append(ps[j - 1] + a[j])
print(ps)
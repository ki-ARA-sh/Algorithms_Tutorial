Set = [1, 2, 3]
n = 3
# 1<<n = 2**n (in PYTHON)
for mask in range(1 << n):
    for i in range(n):
        if mask & (1 << i):
            print(Set[i], end=' ')
    print()

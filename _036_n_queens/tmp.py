n = 5
for m in range(n ** 2):
    i = (n * m) // n ** 2
    j = m - i * n
    print(i, j)
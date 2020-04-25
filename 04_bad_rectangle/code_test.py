n = int(input())
result = 0
for a in range(1, n + 1):
    for b in range(a, n - a + 1):
        c = n - a - b
        if (a + b > c) and (c >= b):
            result += 1
print(result)
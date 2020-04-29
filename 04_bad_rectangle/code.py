n = int(input())
result = 0
for a in range(1, n // 3 + 1):
    # because a is the smallest and it could not be greater than /3
    result = result + (n - 3 * a) // 2 - max(0, n // 2 - 2 * a + 1) + 1
result = result % int(1e9 + 7)
print(result)
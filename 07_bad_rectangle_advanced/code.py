n = int(input())
result = 0

bound = (n // 2 + 1) // 2
result = bound * (bound + 1) - (n // 2) * bound + (n // 3) - bound
k = (n // 3) // 2
result = result + (n + 1) * k - 3 * k * (k + 1)
if (n // 3) % 2 == 1:
    result = result + (n - 3 * (2 * k + 1)) // 2
result = result % int(1e9 + 7)
print(result)

n = int(input())
result = 0
i = 1
while i * i <= n:
    if (n % i) == 0:
        if i * i == n:
            result += 1
        else:
            result += 2
    i = i + 1

print(result)


n, k = map(int, input().split())

pattern = [[]] * n
for i in range(n):
    pattern[i] = list(input())


result = [[]] * (n ** k)
for i in range(n ** k):
    result[i] = list(input())


print(pattern)
print(result)
n = int(input())
M = 1000000007
numbers = input().split()
# numbers = [int(a_number) for a_number in input().split()]
# answer = (sum(numbers) % M) * ((2 ** (n - 1)) % M) % M
# answer = 0
# for i in range(n):
#     answer = answer + int(numbers[i] * (2 ** (n - 1)))
answer = 0
power_of_two = 1
for i in range(1, n):
    power_of_two = (2 * power_of_two) % M
for a_number in numbers:
    answer = (answer + int(a_number)) % M
answer = (answer * power_of_two) % M
print(answer)

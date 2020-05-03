import math


def divide_set(n, a_set):
    total = 0
    for i in range(n):
        total = total + a_set[i]
    min_diff = math.inf
    for mask in range(1 << (n - 1)):
        sub_sum = 0
        for i in range(n):
            if mask & (1 << i):
                sub_sum = sub_sum + a_set[i]
        if abs(total - 2 * sub_sum) < min_diff:
            min_diff = abs(total - 2 * sub_sum)
    return min_diff


def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    print(divide_set(n, a))


if __name__ == '__main__':
    main()


def get_max_subrange_nonoptimal(n, a):
    result = -1 * (1e9 + 7)
    for i in range(1, n + 1):
        for l in range(0, n - i + 1):
            val = 0
            for k in range(i, i + l):
                val = val + a[k]
            if val > result:
                result = val
    return result


def get_max_subrange_nonoptimal2(n, a):
    result = -1 * (1e9 + 7)
    sums = []
    print(sums)
    for i in range(n):
        sums.append([0] * n)
        sums[i][i] = a[i]
    for l in range(n):
        for r in range(l + 1, n):
            sums[l][r] = sums[l][r - 1] + a[r]
            if sums[l][r] > result:
                result = sums[l][r]
    return result


def get_max_subrange(n, a):
    result = -1 * (1e9 + 7)
    maximum_sums = [0] * n
    maximum_sums[0] = a[0]
    for i in range(1, n):
        maximum_sums[i] = max(a[i], a[i] + maximum_sums[i - 1])
    for i in range(n):
        result = max(result, maximum_sums[i])
    return result


def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(get_max_subrange(n, a))


if __name__ == '__main__':
    main()
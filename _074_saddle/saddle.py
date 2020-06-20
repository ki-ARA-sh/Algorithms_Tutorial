

def is_saddle(i, j, a):
    result = True
    result = result and (a[i - 1][j] < a[i][j])
    result = result and (a[i + 1][j] < a[i][j])
    result = result and (a[i][j + 1] > a[i][j])
    result = result and (a[i][j - 1] > a[i][j])
    if not result:
        result = True
        result = result and (a[i - 1][j] > a[i][j])
        result = result and (a[i + 1][j] > a[i][j])
        result = result and (a[i][j + 1] < a[i][j])
        result = result and (a[i][j - 1] < a[i][j])
    return result


def main():
    n, m = map(int, input().split())
    a = [None] * n
    for i in range(n):
        a[i] = list(map(int, input().split()))
    result = 0
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if is_saddle(i, j, a):
                result += 1
    print(result)


if __name__ == '__main__':
    main()

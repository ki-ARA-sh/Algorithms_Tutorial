
def fractal(pattern, n, k, blank):
    if k > 0:
        result = [[]] * (n ** k)
        for i in range(n):
            row = i * (n ** (k - 1))
            for j in range(n):
                segment = fractal(pattern, n, k - 1, blank and (pattern[i][j] == '.'))
                for m in range(n ** (k - 1)):
                    result[m + row] = result[m + row] + segment[m]
        return result
    else:
        if blank:
            return [['.']]
        else:
            return [['*']]


def main():
    n, k = map(int, input().split())
    pattern = [[]] * n
    for i in range(n):
        pattern[i] = list(input())
    ans = fractal(pattern, n, k, True)
    for row in ans:
        print(''.join(row))


if __name__ == '__main__':
    main()

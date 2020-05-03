def horner(a, n, x, k):
    if k == 0:
        return a[n]
    return x * horner(a, n, x, k - 1) + a[n - k]


def main():
    n, x = map(int, input().split())
    a = [int(x) for x in input().split()]
    print(horner(a, n, x, n))


if __name__ == '__main__':
    main()

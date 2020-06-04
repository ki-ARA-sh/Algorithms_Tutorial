
def f(a, n):
    if n == 1:
        return sum(a)
    mid = 2 ** (n - 1)
    return max(
        max(a[:mid]) + f(a[mid:], n - 1),
        max(a[mid:]) + f(a[:mid], n - 1)
    )


def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(f(a, n))


if __name__ == '__main__':
    main()

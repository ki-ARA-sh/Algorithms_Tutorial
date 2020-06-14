def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    ps = [0 for i in range(n)]
    ps[0] = a[0]
    for i in range(1, n):
        ps[i] = ps[i - 1] + a[i]
    for i in range(q):
        l, r = map(int, input().split())
        print(ps[r] - ps[l] + a[l])
        pass


if __name__ == '__main__':
    main()
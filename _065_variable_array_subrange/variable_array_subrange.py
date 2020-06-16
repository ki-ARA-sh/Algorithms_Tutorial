
def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    ps = [0 for i in range(n)]
    ps[0] = a[0]
    for i in range(1, n):
        ps[i] = ps[i - 1] + a[i]
    for i in range(q):
        row = list(map(int, input().split()))
        if row[0] == 1:
            l = row[1]
            r = row[2]
        elif row[0] == 2:
            idx = row[1]
            nv = row[2]
        pass


if __name__ == '__main__':
    main()
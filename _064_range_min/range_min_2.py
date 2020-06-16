def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(q):
        l, r = map(int, input().split())
        print(min(a[l:(r+1)]))
    pass


if __name__ == '__main__':
    main()
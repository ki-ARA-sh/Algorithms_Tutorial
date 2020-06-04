
def peak(a, l, r):
    if r - l == 1:
        return l
    mid = (l + r) // 2
    if a[mid] < a[mid - 1]:
        return peak(a, l, mid)
    else:
        return peak(a, mid, r)


def main():
    # a = [1, 2, 3, 4, 5, 6, 10, 8, 9]
    n = 9
    a = [n - i for i in range(9)]
    print(peak(a, 0, len(a)))


if __name__ == '__main__':
    main()


def count_chocolates(a):
    total = 2 * a[0] - 1
    if a[0] > a[2]:
        total = 2 * a[2]
    ans = [total // 4] * 4
    if total % 4 > 0:
        ans[0] = ans[0] + 1
        if total % 4 > 1:
            ans[1] = ans[1] + 1
            if total % 4 > 2:
                ans[2] = ans[2] + 1
    return ans


def main():
    a = list(map(int, input().split()))
    ans = count_chocolates(a)
    print(' '.join(map(str, ans)))


if __name__ == '__main__':
    main()
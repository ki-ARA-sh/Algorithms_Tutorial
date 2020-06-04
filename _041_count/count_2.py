from bisect import bisect as upper_bound


def count_k(arr, n, k):
    # Variable to store final answer
    ans = 0

    # Loop to find prefix-sum
    for i in range(1, n):
        arr[i] += arr[i - 1]
        if (arr[i] > k or arr[i] < -1 * k):
            ans += 1

    if (arr[0] > k or arr[0] < -1 * k):
        ans += 1

    # Sorting prefix-sum array
    arr = sorted(arr)

    # Loop to find upper_bound
    # for each element
    for i in range(n):
        ans += n - upper_bound(arr, arr[i] + k)

        # Returning final answer
    return ans
    # ans = 0
    # for i in range(1, n):
    #     a[i] += a[i - 1]
    #     if abs(a[i]) > k:
    #         ans += 1
    # if abs(a[0]) > k:
    #     ans += 1
    # a = sorted(a)
    # if i in range(n):
    #     ans += n - upper_bound(a, a[i] + k)
    # return ans


def main():
    m = int(input())
    ans = [0 for i in range(m)]
    for i in range(m):
        n, k = map(int, input().split())
        a = list(map(int, input().split()))
        # ps = get_ps(a, n)
        ans[i] = count_k(a, n, k)
    print('\n'.join(list(map(str, ans))))


if __name__ == '__main__':
    main()

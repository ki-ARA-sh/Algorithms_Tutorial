from bisect import bisect_left as lower_bound


def count_displacements(a, n):
    ans = 0
    for i in range(0, n - 1):
        ans += lower_bound(sorted(a[i + 1:]), a[i])
    return ans


def merge(left, right):
    ans = 0
    i = 0
    j = 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            ans += len(left) - i
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result, ans


def count_misplacements(a):
    if len(a) == 1:
        return a, 0
    mid = len(a) // 2
    left, x = count_misplacements(a[:mid])
    right, y = count_misplacements(a[mid:])
    arr, z = merge(left, right)
    return arr, x + y + z


def main():
    n = int(input())
    a = list(map(int, input().split()))
    b, x = count_misplacements(a)
    print(x)


if __name__ == '__main__':
    main()

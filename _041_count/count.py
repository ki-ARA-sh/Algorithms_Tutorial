
def binary_search(ps, base, left, right, k, n):
    if right - left <= 0:
        if ps[left] - ps[base] > k:
            return 0
        return n
    mid = left + (right - left) // 2
    if ps[mid] - ps[base] <= k < ps[mid + 1] - ps[base]:
        return mid - base
    elif ps[mid] - ps[base] > k:
        return binary_search(ps, base, left, mid - 1, k, n)
    else:
        return binary_search(ps, base, mid + 1, right, k, n)


def search_binary(ps, base, left, right, k):
    if right <= left:
        if ps[max(left, right)] - ps[base] > k:
            return len(ps) - base - 1
        else:
            return 0
    mid = left + (right - left) // 2
    if abs(ps[mid] - ps[base]) <= k < abs(ps[mid + 1] - ps[base]):
        return len(ps) - mid - 1
    elif abs(ps[mid] - ps[base]) > k:
        return search_binary(ps, base, left, mid - 1, k)
    else:
        return search_binary(ps, base, mid + 1, right, k)


def count_k(ps, n, k):
    ans = 0
    for i in range(n):
        ans += search_binary(ps, i, i + 1, n, k)
        # ans += n - binary_search(ps, i, i + 1, n, k, n - i) - i
    return ans


def search_binary_2(ps, left, right, k):
    if right <= left:
        if ps[left] > k:
            return len(ps)
        else:
            return 0
    mid = left + (right - left) // 2
    if ps[mid] <= k < ps[mid + 1]:
        return len(ps) - mid - 1
    elif ps[mid] > k:
        return search_binary_2(ps, left, mid - 1, k)
    else:
        return search_binary_2(ps, mid + 1, right, k)


def count_k_2(ps, n, k):
    ans = 0
    for i in range(n):
        ans += search_binary_2(ps[i + 1:], 0, n - i - 1, k + ps[i])
        # ans += search_binary_2([ps[j] - ps[i] for j in range(i + 1, n + 1)], 0, n - i - 1, k)
        # ans += search_binary(ps, i, i + 1, n, k)
        # ans += n - binary_search(ps, i, i + 1, n, k, n - i) - i
    return ans


def get_ps(a, n):
    ps = [0]
    for i in range(n):
        ps.append(ps[i] + a[i])
    ps.sort()
    return ps


def main():
    m = int(input())
    ans = [0 for i in range(m)]
    for i in range(m):
        n, k = map(int, input().split())
        a = list(map(int, input().split()))
        ps = get_ps(a, n)
        ans[i] = count_k_2(ps, n, k)
    print('\n'.join(list(map(str, ans))))


if __name__ == '__main__':
    main()

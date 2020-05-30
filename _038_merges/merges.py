
def merges_divided(arrays):
    if len(arrays) == 1:
        return arrays[0]
    mid = len(arrays) // 2
    arr1 = merges_divided(arrays[:mid])
    arr2 = merges_divided(arrays[mid:])
    result = []
    p1 = 0
    p2 = 0
    while p1 < len(arr1) or p2 < len(arr2):
        if p1 == len(arr1):
            result.append(arr2[p2])
            p2 += 1
            continue
        elif p2 == len(arr2):
            result.append(arr1[p1])
            p1 += 1
            continue
        if arr1[p1] < arr2[p2]:
            result.append(arr1[p1])
            p1 += 1
        else:
            result.append(arr2[p2])
            p2 += 1
        pass
    return result


def merges(n, k, arrays):
    p = [0 for i in range(k)]
    done = False
    result = []
    while not done:
        result.append(float("inf"))
        index = -1
        for i in range(k):
            if p[i] < n and result[-1] > arrays[i][p[i]]:
                result[-1] = arrays[i][p[i]]
                index = i
        p[index] += 1
        done = True
        for i in p:
            done = done and (i == n)
    return result


def main():
    n, k = map(int, input().split())
    arrays = []
    for i in range(k):
        arrays.append(list(map(int, input().split())))
    # result = merges(n, k, arrays)
    result = merges_divided(arrays)
    print(' '.join(list(map(str, result))))


if __name__ == '__main__':
    main()

import math


def get_segment_index(index, T):
    return index // T


def main():
    n, q = list(map(int, input().split()))
    T = int(math.sqrt(n))
    a = list(map(int, input().split()))

    neg_inf = float('-inf')
    MAX_N = math.ceil(n / T)
    maximums = [neg_inf] * MAX_N
    for i in range(MAX_N):
        maximums[i] = max(a[(i * T):(min(n, (i + 1) * T))])

    for i in range(q):
        inp = list(map(int, input().split()))
        queryType = inp[0]
        if queryType == 1:
            L = inp[1]
            R = inp[2]

            max_start = get_segment_index(L, T) + 1
            partial_start = True
            if L % T == 0:
                partial_start = False
                max_start -= 1

            max_end = get_segment_index(R, T)
            partial_end = True
            if (R % T == (T - 1)) or (R == (n - 1)):
                partial_end = False
                max_end += 1

            max1 = neg_inf
            if partial_start:
                end_index = min(n, T * (get_segment_index(L, T) + 1))
                max1 = max(a[L:end_index])

            max2 = neg_inf
            if partial_end:
                start_index = T * get_segment_index(R, T)
                max2 = max(a[start_index:(R + 1)])

            max3 = max(maximums[max_start:max_end])

            print(max(max1, max2, max3))
        else:
            idx = inp[1]
            nv = inp[2]
            a[idx] = nv
            index = get_segment_index(idx, T)
            maximums[index] = max(a[(T * index):(min(n, T * (index + 1)))])


if __name__ == '__main__':
    main()
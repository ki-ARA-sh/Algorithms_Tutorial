
def are_ranges_independent(range1, range2):
    return range1[1] > range2[0]


def count_max_independent_ranges(ranges):
    for i in range(len(ranges) - 1):
        if are_ranges_independent(ranges[0], ranges[i + 1]):
            return 1 + count_max_independent_ranges(ranges[(i + 1):])
    return 0


def count_max_ranges(ranges):
    last_r = -1
    ans = 0
    for i in range(len(ranges)):
        if last_r <= ranges[i][0]:
            last_r = ranges[i][1]
            ans = ans + 1
    return ans


def main():
    n = int(input())
    a = list(map(int, input().split()))
    ranges = []
    for i in range(len(a) // 2):
        ranges.append([a[2 * i], a[2 * i + 1]])
    ranges = sorted(ranges, key=lambda x: (x[1]))
    print(count_max_ranges(ranges))


if __name__ == '__main__':
    main()


def get_largest_subtable(table, m, n):
    result = -1000000001
    for r1 in range(m):
        b = [0] * n
        for r2 in range(r1 + 1, m + 1):
            for i in range(n):
                b[i] = b[i] + table[r2 - 1][i]
            sum_max = [0] * n
            sum_max[0] = b[0]
            for i in range(1, n):
                sum_max[i] = max(b[i], b[i] + sum_max[i - 1])
            for i in range(n):
                result = max(result, sum_max[i])
    return result


def main():
    m, n = map(int, input().split())
    table = list()
    for i in range(m):
        table.append(list(map(int, input().split())))
    print(get_largest_subtable(table, m, n))


if __name__ == '__main__':
    main()

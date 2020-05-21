
def sum_from_origin(table):
    result = list()
    if len(table) > 0:
        result = [[0 for j in range(len(table[0]))] for i in range(len(table))]
        for i in range(len(result)):
            for j in range(len(result[i])):
                a = 0
                b = 0
                c = 0
                if i > 0:
                    a = result[i - 1][j]
                if j > 0:
                    b = result[i][j - 1]
                if (i > 0) and (j > 0):
                    c = result[i - 1][j - 1]
                result[i][j] = a + b - c + table[i][j]
    return result


def get_largest_subtable(table):
    pass


def main():
    m, n = map(int, input().split())
    table = list()
    for i in range(m):
        table.append(list(map(int, input().split())))
    #print(get_largest_subtable(table))
    print(sum_from_origin(table))


if __name__ == '__main__':
    main()

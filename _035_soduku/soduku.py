
def get_blanks(table):
    result = []
    for i in range(9):
        for j in range(9):
            if table[i][j] == 0:
                result.append([i, j])
    return result


def check_table(table, row, column, value):
    for i in range(9):
        if i != column and table[row][i] == value:
            return False
        if i != row and table[i][column] == value:
            return False
    for i in range(3 * (row // 3), 3 + 3 * (row // 3)):
        for j in range(3 * (column // 3), 3 + 3 * (column // 3)):
            if (i != row and j != column) and table[i][j] == value:
                return False
    return True


def solve_soduku(table, blanks):
    result = True
    if len(blanks) > 0:
        result = False
        for i in range(1, 10):
            if check_table(table, blanks[0][0], blanks[0][1], i):
                table[blanks[0][0]][blanks[0][1]] = i
                result = result or solve_soduku(table, blanks[1:])
                if result:
                    break
                table[blanks[0][0]][blanks[0][1]] = 0
    return result


def print_table(table, result):
    if not result:
        print('No solution exists')
    else:
        for row in table:
            a = list(map(str, row))
            print(' '.join(a))


def main():
    table = []
    for i in range(9):
        table.append(list(map(int, input().split())))
    blanks = get_blanks(table)
    result = solve_soduku(table, blanks)
    print_table(table, result)


if __name__ == '__main__':
    main()

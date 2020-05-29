
def check_board(n, board, row, column):
    acceptable_range = [i for i in range(n)]
    if 1 in board[row]:
        return False
    for i in range(n):
        if i != row:
            if board[i][column] == 1:
                return False
            if (abs(row - i) + column) in acceptable_range:
                if board[i][abs(row - i) + column] == 1:
                    return False
            if (-abs(row - i) + column) in acceptable_range:
                if board[i][-abs(row - i) + column] == 1:
                    return False
    return True


def n_queens(start, n, board, k):
    if k == 0:
        return 1
    result = 0
    for m in range(start, n ** 2):
        i = (n * m) // n ** 2
        j = m - i * n
        if board[i][j] == 0:
            if check_board(n, board, i, j):
                board[i][j] = 1
                result = result + n_queens(m + 1, n, board, k - 1)
                board[i][j] = 0
    return result


def main():
    n, k = map(int, input().split())
    board = [[0 for i in range(n)] for j in range(n)]
    print(n_queens(0, n, board, k))


if __name__ == '__main__':
    main()

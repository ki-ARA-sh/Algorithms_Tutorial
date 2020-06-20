from enum import Enum
import sys
sys.setrecursionlimit(10**6)


class BlockStatus(Enum):
    NotDetermined = 0
    Neither = 1
    Summit = 2
    Valley = 3
    InnerCell = 4


def get_adjacents(v, n):
    result = [(-1, -1)] * 8
    r = v[0]
    c = v[1]
    r_f = (r + 1) <= (n - 1)
    r_b = (r - 1) >= 0
    c_f = (c + 1) <= (n - 1)
    c_b = (c - 1) >= 0
    counter = 0
    if r_f:
        result[counter] = (r + 1, c)
        counter += 1
    if r_b:
        result[counter] = (r - 1, c)
        counter += 1
    if c_f:
        result[counter] = (r, c + 1)
        counter += 1
    if c_b:
        result[counter] = (r, c - 1)
        counter += 1
    if r_f and c_f:
        result[counter] = (r + 1, c + 1)
        counter += 1
    if r_f and c_b:
        result[counter] = (r + 1, c - 1)
        counter += 1
    if r_b and c_f:
        result[counter] = (r - 1, c + 1)
        counter += 1
    if r_b and c_b:
        result[counter] = (r - 1, c - 1)
        counter += 1
    return result[:counter]


def change_block_status(old_status, new_status):
    if old_status == BlockStatus.NotDetermined:
        return new_status
    elif new_status == BlockStatus.NotDetermined:
        return old_status
    elif old_status == BlockStatus.InnerCell:
        return new_status
    elif new_status == BlockStatus.InnerCell:
        return old_status
    elif (old_status == BlockStatus.Neither) or (new_status == BlockStatus.Neither):
        return BlockStatus.Neither
    elif old_status == BlockStatus.Summit and new_status == BlockStatus.Valley:
        return BlockStatus.Neither
    elif old_status == BlockStatus.Valley and new_status == BlockStatus.Summit:
        return BlockStatus.Neither
    elif old_status == BlockStatus.Summit and new_status == BlockStatus.Summit:
        return BlockStatus.Summit
    elif old_status == BlockStatus.Valley and new_status == BlockStatus.Valley:
        return BlockStatus.Valley


def dfs(v, a, n, mark):
    mark[v[0]][v[1]] = True
    adj = get_adjacents(v, n)
    result = BlockStatus.NotDetermined
    for u in adj:
        if (not mark[u[0]][u[1]]) and (a[u[0]][u[1]] == a[v[0]][v[1]]):
            result = change_block_status(result, dfs(u, a, n, mark))
        if a[u[0]][u[1]] < a[v[0]][v[1]]:
            result = change_block_status(result, BlockStatus.Summit)
        elif a[u[0]][u[1]] > a[v[0]][v[1]]:
            result = change_block_status(result, BlockStatus.Valley)
    return result


def main():
    n = int(input())
    a = [None] * n
    for i in range(n):
        a[i] = list(map(int, input().split()))
    mark = [[False for i in range(n)] for j in range(n)]
    summit_num = 0
    valley_num = 0
    for i in range(n):
        for j in range(n):
            if not mark[i][j]:
                status = dfs((i, j), a, n, mark)
                if status == BlockStatus.Summit:
                    summit_num += 1
                elif status == BlockStatus.Valley:
                    valley_num += 1
    print(str(summit_num) + ' ' + str(valley_num))


def check_adjacent():
    n = int(input())
    a = [None] * n
    for i in range(n):
        a[i] = list(map(int, input().split()))
    for i in range(n):
        row = []
        for j in range(n):
            row.append(len(get_adjacents((i, j), n)))
        print(' '.join(map(str, row)))


if __name__ == '__main__':
    main()


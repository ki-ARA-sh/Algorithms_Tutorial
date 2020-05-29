def generate_move(i, j, n, acceptable_range):
    # acceptable_range = [k for k in range(n)]
    result = []
    if (i + 2) in acceptable_range and (j + 1) in acceptable_range:
        result.append((i + 2, j + 1))
    if (j + 2) in acceptable_range and (i + 1) in acceptable_range:
        result.append((i + 1, j + 2))
    if (j + 2) in acceptable_range and (i - 1) in acceptable_range:
        result.append((i - 1, j + 2))
    if (i - 2) in acceptable_range and (j + 1) in acceptable_range:
        result.append((i - 2, j + 1))
    if (i - 2) in acceptable_range and (j - 1) in acceptable_range:
        result.append((i - 2, j - 1))
    if (j - 2) in acceptable_range and (i - 1) in acceptable_range:
        result.append((i - 1, j - 2))
    if (j - 2) in acceptable_range and (i + 1) in acceptable_range:
        result.append((i + 1, j - 2))
    if (i + 2) in acceptable_range and (j - 1) in acceptable_range:
        result.append((i + 2, j - 1))
    return result


def horse_moves(start, n, k, acceptable_range):
    if k == 0:
        a_set = set()
        a_set.add(start)
        return a_set
    moves = generate_move(start[0], start[1], n, acceptable_range)
    result = set()
    for a_move in moves:
        cells = horse_moves(a_move, n, k - 1, acceptable_range)
        result = result | cells
        # for a_cell in cells:
        #     if a_cell not in result:
        #         result.append(a_cell)
    return result


def main():
    n, k = map(int, input().split())
    print(len(horse_moves((0, 0), n, k, [k for k in range(n)])))


if __name__ == '__main__':
    main()

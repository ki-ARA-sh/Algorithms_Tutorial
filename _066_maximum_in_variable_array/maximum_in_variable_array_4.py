

# def get_max_matrix(n, a):
#     result = [[0 for j in range(n - i)] for i in range(n)]
#     for i in range(n):
#         result[i][0] = a[i]
#         for j in range(i + 1, n):
#             result[i][j - i] = max(result[i][j - i - 1], a[j])
#     return result
#

def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    # matrix = get_min_matrix(n, a)
    for i in range(q):
        row = list(map(int, input().split()))
        if row[0] == 1:
            print(max(a[row[1]:(row[2] + 1)]))
        else:
            a[row[1]] = row[2]
    pass


if __name__ == '__main__':
    main()

M = 1000000007


def calc_c(max_n):
    c = [[0 for i in range(max_n + 1)] for j in range(max_n + 1)]
    for i in range(max_n + 1):
        for j in range(i + 1):
            if j == 0 or j == i:
                c[i][j] = 1
            else:
                c[i][j] = (c[i - 1][j] + c[i - 1][j - 1]) % M
    return c


def main():
    q = int(input())
    inputs = list()
    max_n = 2000
    c = calc_c(max_n)
    for i in range(q):
        inputs.append(list(map(int, input().split())))
    for i in range(q):
        print(c[inputs[i][0]][inputs[i][1]])


if __name__ == '__main__':
    main()


M = 1000000007


def c(n, r):
    if r > n:
        return 0
    result = (n - r + 1)
    while r > 1:
        result = ((n / r) * result)
        n = n - 1
        r = r - 1
    return int(result) % M
    # if r == 1:
    #     return n % M
    # return ((n / r) * c(n - 1, r - 1)) % M


def main():
    q = int(input())
    answer = list()
    for i in range(q):
        n, r = map(int, input().split())
        answer.append(str(c(n, r)))
        # inputs.append(list(map(int, input().split())))
    print('\n'.join(answer))


if __name__ == '__main__':
    main()

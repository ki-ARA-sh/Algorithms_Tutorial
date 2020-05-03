
def next_in_base(n, k):
    cnt = 0
    p = k + 1
    while p // (10 ** cnt) > 0:
        cnt = cnt + 1
        if (p % (10 ** cnt)) == n * (10 ** (cnt - 1)):
            p = (1 + p // 10) * 10 ** cnt
    return p


def convert_to_base(n, a):
    k = 0
    result = 0
    while a > 0:
        result = result + (a % n) * (10 ** k)
        a = a // n
        k = k + 1
    return result


def f(n):
    base = "1" * n
    base = int(base)
    a = 0
    for i in range(n ** n):
        print(" ".join(str(convert_to_base(n, a) + base)))
        # a = next_in_base(n, a)
        a = a + 1


def main():
    f(int(input()))


if __name__ == '__main__':
    main()

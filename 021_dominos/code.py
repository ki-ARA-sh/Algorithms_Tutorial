
def domino_recursive(n):
    if n < 2:
        return 1
    return (domino_recursive(n - 1) + domino_recursive(n - 2)) % 1000000007


def domino_dynamic(n):
    f_2 = 1
    f_1 = 1
    for i in range(2, n + 1):
        f = (f_1 + f_2) % 1000000007
        f_2 = f_1
        f_1 = f
    return f


def main():
    n = int(input())
    print(domino_dynamic(n))
    # print(domino_recursive(n))


if __name__ == '__main__':
    main()

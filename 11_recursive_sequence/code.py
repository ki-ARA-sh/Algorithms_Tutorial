import sys
sys.setrecursionlimit(100000)


def fn(i):
    if i == 0:
        return 5
    tmp = fn(i - 1)
    if i % 2 == 0:
        return tmp - 21
    else:
        return tmp * tmp


def main():
    print(fn(int(input())))


if __name__ == '__main__':
    main()

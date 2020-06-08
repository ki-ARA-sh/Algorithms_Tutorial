
def count_ways(n):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    return count_ways(n - 1) + count_ways(n - 2) + count_ways(n - 5)


def main():
    print(count_ways(int(input())))


if __name__ == '__main__':
    main()

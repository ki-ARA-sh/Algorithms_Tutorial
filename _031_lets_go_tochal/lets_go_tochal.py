
def get_regular_mountains(n, heights):
    h = sorted(set(heights))
    h = [h.index(i) for i in heights]
    
    pass


def main():
    n = int(input())
    h = list(map(int, input().split()))
    print(get_regular_mountains(n, h))


if __name__ == '__main__':
    main()

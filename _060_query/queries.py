
def main():
    n, q = map(int, input().split())
    sets = [{i + 1} for i in range(n)]
    for i in range(q):
        a_query = input().split()
        if a_query[0] == '1':
            sets[int(a_query[2]) - 1] = sets[int(a_query[2]) - 1] | sets[int(a_query[1]) - 1]
            sets[int(a_query[1]) - 1].clear()
        elif a_query[0] == '2':
            print(len(sets[int(a_query[1]) - 1]))
        elif a_query[0] == '3':
            d = sets[int(a_query[1]) - 1]
            if len(d) > 0:
                print(' '.join(list(map(str, sorted(d)))))
            else:
                print(-1)
    pass


if __name__ == '__main__':
    main()
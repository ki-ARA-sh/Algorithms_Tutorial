

def main():
    n = int(input())
    a = list(map(int, input().split()))
    status = list(map(int, input().split()))
    result = [-1] * n
    counter = 0
    for i in range(n):
        if status[i] == 1:
            result[counter] = a[i]
            counter += 1
    print(' '.join(map(str, sorted(result[:counter]))))
    pass


if __name__ == '__main__':
    main()

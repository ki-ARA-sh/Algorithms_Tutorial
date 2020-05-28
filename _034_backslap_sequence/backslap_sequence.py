
def f(a, b):
    if len(a) == 0:
        return 1
    result = 0
    for item in a[0]:
        if item not in b:
            result += f(a[1:], b + [item])
            # result += f(a[1:], b | {item})
    return result


def main():
    n = int(input())
    a = []
    for i in range(n):
        tmp = input().split()
        tmp = tmp[1:]
        # a.append(set(map(int, tmp)))
        a.append(list(map(int, tmp)))
    # print(f(a, set()))
    print(f(a, list()))


if __name__ == '__main__':
    main()

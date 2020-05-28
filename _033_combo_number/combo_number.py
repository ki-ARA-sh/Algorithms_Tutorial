
def displaced_number(a):
    result = 0
    for i in range(len(a) - 1):
        for j in range(i + 1, len(a)):
            if a[i] > a[j]:
                result += 1
    return result


def f(n, k):
    a = [i + 1 for i in range(n)]
    result = 0
    combinations = g(n, a)
    for a_combo in combinations:
        if displaced_number(a_combo) == k:
            result += 1
    return result


def g(n, a):
    if n == 0:
        return [[]]
    result = []
    for i in range(n):
        b = g(n - 1, a[0:i] + a[(i + 1):n])
        for c in b:
            result.append([a[i]] + c)
    return result



def main():
    n, k = map(int, input().split())
    print(f(n, k))


if __name__ == '__main__':
    main()

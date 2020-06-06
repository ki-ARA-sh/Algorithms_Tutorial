from queue import Queue


def role_models(a):
    my_queue = Queue(maxsize=100000)
    counter = [0] * len(a)
    nonzero = [i + 1 for i in range(len(a))]
    for i in range(len(a)):
        counter[a[i] - 1] += 1
    for i in range(len(a)):
        if counter[i] == 0:
            my_queue.put(i)
    while my_queue.qsize() > 0:
        x = my_queue.get()
        counter[a[x] - 1] -= 1
        if counter[a[x] - 1] == 0:
            my_queue.put(a[x] - 1)
    for i in range(len(a) - 1, -1, -1):
        if counter[i] == 0:
            del nonzero[i]
    return nonzero


def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = role_models(a)
    print(len(ans))
    print(' '.join(list(map(str, ans))))


if __name__ == '__main__':
    main()

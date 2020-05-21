

def doable_tasks(tasks):
    tasks = sorted(tasks)
    time = 0
    for a_task in tasks:
        if time < a_task:
            time = time + 1
    return time


def main():
    n = int(input())
    tasks = list(map(int, input().split()))
    print(doable_tasks(tasks))


if __name__ == '__main__':
    main()

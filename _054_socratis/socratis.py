
def assignment(n, tasks, matrix):
    if n == 1:
        return [tasks[0]], matrix[0][tasks[0]]
    cost = float('inf')
    this_task = -1
    for i in range(n):
        # next_tasks = tasks[0:i] + tasks[(i+1):]
        # next_matrix = matrix[0:i] + matrix[(i+1):]
        next_list, next_cost = assignment(n - 1, tasks[0:i] + tasks[(i+1):], matrix[1:])
        if (next_cost + matrix[0][tasks[i]]) <= cost:
            this_task = [tasks[i]] + next_list
            cost = next_cost + matrix[0][tasks[i]]
    return this_task, cost


def main():
    n = int(input())
    matrix = []
    tasks = [i for i in range(n)]
    for i in range(n):
        matrix.append(list(map(int, input().split())))
    assignments, cost = assignment(n, tasks, matrix)
    print('\n'.join(list(map(str, assignments))))


if __name__ == '__main__':
    main()

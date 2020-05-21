
def f(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    elif n == 3:
        return 2
    else:
        return f(n - 1) + f(n - 2) + f(n - 3) - f(n - 4)


def f_dp(n):
    answer = [0] * 100001
    answer[0] = 1
    answer[1] = 1
    answer[2] = 1
    answer[3] = 2
    for i in range(4, len(answer)):
        answer[i] = (answer[i - 1] + answer[i - 2] + answer[i - 3] - answer[i - 4]) % 1000000007
    return answer
    # if n == 0:
    #     return 1
    # elif n == 1:
    #     return 1
    # elif n == 2:
    #     return 1
    # elif n == 3:
    #     return 2
    # else:
    #     f_0 = 1
    #     f_1 = 1
    #     f_2 = 1
    #     f_3 = 2
    #     answer = 0
    #     for i in range(4, n + 1):
    #         answer = (f_3 + f_2 + f_1 - f_0) % 1000000007
    #         f_0 = f_1
    #         f_1 = f_2
    #         f_2 = f_3
    #         f_3 = answer
    #     return answer


def main():
    q = int(input())
    answers = f_dp(q)
    to_print = list()
    for i in range(q):
        to_print.append(str(answers[int(input())]))
    print('\n'.join(to_print))


if __name__ == '__main__':
    main()

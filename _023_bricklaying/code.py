
def possible_ways(first, second, third):
    result = list()
    result.append([first.copy(), second.copy(), third.copy()])
    result[-1][0].append(True)
    if len(result[-1][0]) >= 2:
        result[-1][1].append(False)
    for i in range(len(second)):
        if not second[i]:
            result.append([first.copy(), second.copy(), third.copy()])
            result[-1][1][i] = True
            if (i == (len(second) - 1)) and (i > 0):
                result[-1][2].append(True)
            if i > 0:
                if result[-1][1][i - 1]:
                    result[-1][2][i - 1] = False
            if i < len(second) - 1:
                if result[-1][1][i + 1]:
                    result[-1][2][i] = False
    for i in range(len(third)):
        if not third[i]:
            result.append([first.copy(), second.copy(), third.copy()])
            result[-1][2][i] = True
    return result


def lay_brick(n, first, second, third):
    if n == 0:
        return 1
    ways = possible_ways(first, second, third)
    result = 0
    for a_way in ways:
        result += lay_brick(n - 1, a_way[0], a_way[1], a_way[2])
    return result


def main():
    q = int(input())
    answers = []
    for i in range(q):
        answers.append(str(lay_brick(int(input()), [], [], [])))
    print('\n'.join(answers))


if __name__ == '__main__':
    main()

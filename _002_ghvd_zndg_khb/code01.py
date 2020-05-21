
def rules_compatible(l_i, r_i, type_i, l_j, r_j, type_j):
    return (type_i != type_j) and (max([l_i, l_j]) < min([r_i, r_j]))


def main():
    result = -1
    m, n = map(int, input().split())
    h = [0] * n
    compatible = True
    lefts = [0] * m
    rights = [0] * m
    types = [0] * m
    for i in range(m):
        lefts[i], rights[i], types[i] = map(int, input().split())
        for j in range(i):
            if (types[i] != types[j]) and (max([lefts[i], lefts[j]]) < min([rights[i], rights[j]])):
                return -1
    if compatible:
        for i in range(2, n):
            for j in range(m):
                if (i > lefts[j]) and (i <= rights[j]):
                    if types[j] == 0:
                        h[i] = h[i - 1] - 1
                    else:
                        h[i] = h[i - 1] + 1
                if not compatible:
                    break
        min_val = min(h)
        min_val = 1 - min_val
        result = ''
        for item in h:
            result = result + ' ' + str(item + min_val)
        result = result[1:]
    return result


if __name__ == '__main__':
    result = main()
    print(result)
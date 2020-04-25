def main():
    n, m = map(int, input().split())
    rules = [-1] * (n - 1)
    rules_are_compatible = True
    for i in range(m):
        l, r, type = map(int, input().split())
        for i in range(l - 1, r - 1):
            if rules[i] == -1:
                rules[i] = type
            elif rules[i] != type:
                rules_are_compatible = False

    if rules_are_compatible:
        prev_rule = 1
        steps = [prev_rule] * n
        min_val = 1
        for i in range(1, n):
            if rules[i - 1] == 1:
                prev_rule = steps[i - 1] + 1
            elif rules[i - 1] == 0:
                prev_rule = steps[i - 1] - 1
                if min_val > prev_rule:
                    min_val = prev_rule
            steps[i] = prev_rule

        for i in range(n):
            steps[i] = steps[i] - min_val + 1

        return ' '.join(str(x) for x in steps)
    else:
        return '-1'


if __name__ == "__main__":
    print(main())

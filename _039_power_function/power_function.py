def power_function(base, exp):
    if exp == 0:
        return 1
    result = power_function(base, exp // 2)
    if exp % 2 == 1:
        result = result * result * base
    else:
        result = result * result
    return result


def main():
    base = float(input())
    exp = int(input())
    print('{:.3f}'.format(power_function(base, exp)))


if __name__ == '__main__':
    main()

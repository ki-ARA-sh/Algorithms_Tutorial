import time


def change_base(x):
    c = [0, 1, 2, 4, 6, 8, 9]
    y = 0
    current_power_of_ten = 1
    while x > 0:
        y = y + current_power_of_ten * c[x % 7]
        x = x // 7
        current_power_of_ten = current_power_of_ten * 10
    return y


def get_sum(x):
    sum_of_digits = 0
    while x > 0:
        sum_of_digits = (sum_of_digits + (x % 10)) % 11
        x = x // 10
    return sum_of_digits


def count_number_of_eligible(k):
    answer = 0

    cntA = [0] * 11
    cntB = [0] * 11

    for x in range(7 ** (k // 2)):
        cntA[get_sum(change_base(x)) - 1] = cntA[get_sum(change_base(x)) - 1] + 1
    for x in range(7 ** ((k // 2 + 1) if (k % 2 != 0) else k // 2)):
        cntB[get_sum(change_base(x)) - 1] = cntB[get_sum(change_base(x)) - 1] + 1
    for i in range(11):
        answer = answer + cntA[i] * cntB[i]

    return answer


def main():
    k = int(input())
    # start_time = time.time()
    print(count_number_of_eligible(k))
    # print('Running time is %s seconds' % (time.time() - start_time))


if __name__ == "__main__":
    main()

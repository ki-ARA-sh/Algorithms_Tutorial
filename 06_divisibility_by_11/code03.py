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


def count_number_of_eligible(k):
    answer = 0
    for x in range(7 ** k):
        if (change_base(x) % 11) == 0:
            answer += 1
    return answer


def main():
    k = int(input())
    start_time = time.time()
    print(count_number_of_eligible(k))
    print('Running time is %s seconds' % (time.time() - start_time))


if __name__ == "__main__":
    main()

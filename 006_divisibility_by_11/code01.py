import time

def check(x):
    if x % 11 > 0:
        return False
    while x > 0:
        if (x % 10) in {3, 5, 7}:
            return False
        x = x // 10
    return True


def count_number_of_eligible(k):
    answer = 0
    for x in range(10 ** k):
        if check(x):
            answer += 1
    return answer


def main():
    k = int(input())
    start_time = time.time()
    print(count_number_of_eligible(k))
    print('Running time is %s seconds' % (time.time() - start_time))


if __name__ == "__main__":
    main()

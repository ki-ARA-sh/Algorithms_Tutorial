from math import ceil
import heapq


def get_medians(n, numbers):
    top_half = []
    bottom_half = []
    result = [0] * n
    for i in range(n):
        if ceil((i + 1) / 2) > len(bottom_half):
            x = heapq.heappushpop(top_half, numbers[i])
            heapq.heappush(bottom_half, -1 * x)
        else:
            x = heapq.heappushpop(bottom_half, -1 * numbers[i])
            heapq.heappush(top_half, -1 * x)
        result[i] = -1 * bottom_half[0]
    return result


def main():
    n = int(input())
    numbers = [0] * n
    for i in range(n):
        numbers[i] = int(input())
    medians = get_medians(n, numbers)
    print('\n'.join(list(map(str, medians))))


if __name__ == '__main__':
    main()


from bisect import bisect_left as lower_bound
import heapq


def main():
    q = int(input())
    names = []
    customers_list = [dict() for i in range(q)]
    for i in range(q):
        row = input().split()
        k = int(row[0])
        for j in range(k):
            names.append(row[2 * j + 1])
            customers_list[i][row[2 * j + 1]] = int(row[2 * j + 2])
    names.sort()
    mark = [False for i in range(len(names))]
    id_heap = []
    day_heap = []
    for i in range(q):
        for a_name, remaining_days in customers_list[i].items():
            index = lower_bound(names, a_name)
            heapq.heappush(id_heap, (index, remaining_days + i))
            heapq.heappush(day_heap, (remaining_days + i, index))
        result = []
        while (len(day_heap) > 0) and (day_heap[0][0] == i + 1):
            index = day_heap[0][1]
            heapq.heappop(day_heap)
            if not mark[index]:
                mark[index] = True
                result.append(names[index])
        while (len(id_heap) > 0) and mark[id_heap[0][0]]:
            heapq.heappop(id_heap)

        if len(id_heap) > 0:
            index = id_heap[0][0]
            mark[index] = True
            result.append(names[index])
            heapq.heappop(id_heap)

        print(' '.join(sorted(result)))


if __name__ == '__main__':
    main()

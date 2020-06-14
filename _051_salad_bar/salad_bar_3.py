import heapq


def manage_bar(q, daily_customers, sorted_names):
    day_heap = []
    numbers_heap = []
    result = [''] * q
    mark = [False] * len(sorted_names)
    for i in range(q):
        today_expiries = []
        for j in range(daily_customers[i][0]):
            name_index = sorted_names.index(daily_customers[i][1][j][0])
            heapq.heappush(numbers_heap, name_index)
            heapq.heappush(day_heap, (i + daily_customers[i][1][j][1], name_index))
            # heapq.heappush(numbers_heap, (name_index, i + daily_customers[i][1][j][1], daily_customers[i][1][j][0]))
            # heapq.heappush(day_heap, (i + daily_customers[i][1][j][1], daily_customers[i][1][j][0], name_index))
        while len(day_heap) > 0 and mark[day_heap[0][1]]:
            heapq.heappop(day_heap)
        while len(day_heap) > 0 and (day_heap[0][0] == (i + 1)):
            expired_customer = heapq.heappop(day_heap)
            today_expiries = today_expiries + [sorted_names[expired_customer[1]]]
            mark[expired_customer[1]] = True
            # numbers_heap.remove((expired_customer[2], expired_customer[0], expired_customer[1]))
            # heapq.heapify(numbers_heap)
        while len(numbers_heap) > 0 and mark[numbers_heap[0]]:
            heapq.heappop(numbers_heap)
        if len(numbers_heap) > 0:
            removed_index = heapq.heappop(numbers_heap)
            mark[removed_index] = True
            # day_heap.remove((removed_index[1], removed_index[2], removed_index[0]))
            today_expiries = today_expiries + [sorted_names[removed_index]]
        result[i] = ' '.join(sorted(today_expiries))
    return result


def main():
    q = int(input())
    customers = [None] * q
    sorted_names = []
    for i in range(q):
        day = input().split()
        day_customers = (int(day[0]), [None] * int(day[0]))
        for j in range(day_customers[0]):
            day_customers[1][j] = (day[2 * j + 1], int(day[2 * j + 2]))
            sorted_names.append(day[2 * j + 1])
        # customers.append(day_customers)
        customers[i] = day_customers
    # sorted_names.sort()
    daily_expired_customers = manage_bar(q, customers, sorted(sorted_names))
    print('\n'.join(daily_expired_customers))


if __name__ == '__main__':
    main()

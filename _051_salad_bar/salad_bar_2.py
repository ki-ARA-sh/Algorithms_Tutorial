import heapq
# myHeap = [3, 1, 5]
# heapq.heapify(myHeap) # make a heap with elements of (myHeap = [3, 1, 5]) and store it in myHeap
# heapq.heappush(myHeap, -5) # add -5 to myHeap
# minElement =  heapq.heappop(myHeap)  # pop min element in myHeap and return value of min elemnt
# print(minElement) # print -5


def manage_bar(q, daily_customers, sorted_names):
    day_heap = []
    numbers_heap = []
    result = [''] * q
    for i in range(q):
        today_expiries = []
        for j in range(daily_customers[i][0]):
            name_index = sorted_names.index(daily_customers[i][1][j][0])
            heapq.heappush(numbers_heap, (name_index, i + daily_customers[i][1][j][1], daily_customers[i][1][j][0]))
            heapq.heappush(day_heap, (i + daily_customers[i][1][j][1], daily_customers[i][1][j][0], name_index))
        while len(day_heap) > 0 and (day_heap[0][0] == (i + 1)):
            expired_customer = heapq.heappop(day_heap)
            today_expiries = today_expiries + [expired_customer[1]]
            numbers_heap.remove((expired_customer[2], expired_customer[0], expired_customer[1]))
            heapq.heapify(numbers_heap)
        if len(numbers_heap) > 0:
            removed_index = heapq.heappop(numbers_heap)
            day_heap.remove((removed_index[1], removed_index[2], removed_index[0]))
            today_expiries = today_expiries + [removed_index[2]]
        result[i] = ' '.join(sorted(today_expiries))
    return result


def main():
    q = int(input())
    customers = []
    sorted_names = []
    for i in range(q):
        day = input().split()
        day_customers = (int(day[0]), [])
        for j in range(day_customers[0]):
            day_customers[1].append((day[2 * j + 1], int(day[2 * j + 2])))
            sorted_names.append(day[2 * j + 1])
        customers.append(day_customers)
    sorted_names.sort()
    daily_expired_customers = manage_bar(q, customers, sorted_names)
    print('\n'.join(daily_expired_customers))


if __name__ == '__main__':
    main()

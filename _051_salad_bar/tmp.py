import heapq


# myheap = [10 - i for i in range(10)]
# heapq.heapify(myheap)
# print(myheap)
# heapq.heappush(myheap, -1)
# print(myheap)
# heapq.heappop(myheap)
# print(myheap)

q = 4
customers = ["3 hamid 1 ali 4 rayan 2", "2 asgharparande 2 kamid 3", "2 keytwo 2 arezoo 2", "1 keyone 1"]
customers_list = []
for i in range(q):
    this_day = customers[i].split()
    num = int(this_day[0])
    for j in range(num):
        customers_list.append((this_day[2 *j + 2], this_day[2 * j + 1]))
    heapq.heapify(customers_list)
    while customers_list[0] == 1:
        # customer_info =
        pass



    for key, value in customers_list:
        customers[key] = value - 1



def manage_bar(q, names, days):
    names_heap = []
    days_heap = []
    result = [[]] * q
    for d in range(1, q + 1):
        pass
    return result


def main():
    q = int(input())
    days = []
    customers_names = []
    for i in range(q):
        day = input().split()
        a_dict = dict()
        for j in range(int(day[0])):
            a_dict[day[2 * j + 1]] = int(day[2 * j + 2])
            customers_names.append(day[2 * j + 1])
        days.append(a_dict)
    customers_names.sort()
    result = manage_bar(q, customers_names, days)
    for row in result:
        print(' '.join(row))


if __name__ == '__main__':
    main()

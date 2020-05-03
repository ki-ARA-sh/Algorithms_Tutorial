
def n_tuple(n, prefix, k):
    # Base condition --number of choices equal to length of n--
    if k == 0:
        print(prefix)
        return
    for i in range(n):
        new_prefix = prefix + str(i + 1)
        # Append current number(i) to prefix and select k-1 other number
        n_tuple(n, new_prefix + ' ', k - 1)


m = int(input())
n_tuple(m, '', m)

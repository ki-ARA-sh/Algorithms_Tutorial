
def subSets(Set, sub_set, n, k):
    if k == n:
        for i in range(n):
            if sub_set[i] != -1:
                print(sub_set[i], end=' ')
        print()
        return
    sub_set[k] = -1
    subSets(Set, sub_set, n, k+1)

    sub_set[k] = Set[k]
    subSets(Set, sub_set, n, k+1);

a = [1, 2, 3]
b = [1, 2, 3]
subSets(a, b, 3, 0)
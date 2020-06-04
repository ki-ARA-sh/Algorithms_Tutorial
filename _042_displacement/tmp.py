
def merge(left):
    for i in range(len(left)):
        left[i] = 0
    return -1


n = 11
a = [1 for i in range(n)]
mid = n // 2
merge(a)
print(a)
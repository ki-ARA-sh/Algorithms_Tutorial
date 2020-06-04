
def binary_search(a, l, r, x):
    if r - l <= 0:
        return -1
    mid = (l + r) // 2
    if a[mid] == x:
        return mid
    elif a[mid] > x:
        return binary_search(a, l, mid - 1, x)
    else:
        return binary_search(a, mid + 1, r, x)



def main():
    pass


if __name__ == '__main__':
    main()

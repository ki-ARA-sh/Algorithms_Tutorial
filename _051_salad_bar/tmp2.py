from bisect import bisect_left as lower_bound


a = ['a', 'z', 'g', 'd', 'd', 'e', 'w']
a.sort()
print(a)
while True:
    word = input()
    print(lower_bound(a, word))
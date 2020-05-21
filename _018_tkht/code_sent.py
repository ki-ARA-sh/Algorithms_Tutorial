n,c=map(int,input().split())
chocolates=list(map(int,input().split()))
#Sort 'chocolates' in decreasing order :reverse=True:
chocolates.sort(reverse=True)
for choco in chocolates:
    c-=min(c, max(0, choco-c))
print(c)
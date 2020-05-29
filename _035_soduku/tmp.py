def f(b):
    b[0] = 10

a = [i for i in range(10)]
f(a)
print(a)
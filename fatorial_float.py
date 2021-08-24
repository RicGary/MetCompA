def fatorial(x):
    f = 1.0
    n = x + 1.0
    while n != 1:
        n = n - 1
        f *= n
    print(f)
fatorial(5)
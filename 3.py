def lagr(n, t):
    a = []
    w = 1
    nn = n
    d = t
    while n > 0 and w:
        s = int(n ** (1/3)) - t
        t = 0
        n -= s ** 3
        a.append(s ** 3)
        if d > s:
            print(0)
            w = 0
        if len(a) > 7 and w:
            a.clear()
            lagr(nn, d + 1)
            w = 0
    if w: print(*a)
lagr(int(input()), 0)

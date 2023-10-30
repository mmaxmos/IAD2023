def lagr(n, t):
    a = []
    w = 1
    nn = n
    d = t
    while n > 0 and w:
        s = int(n ** 0.5) - t 
        t = 0
        n -= s ** 2
        a.append(s)
        if len(a) == 5:
            a.clear()
            lagr(nn, d + 1)
            w = 0
    if w: print(*a)
lagr(int(input()), 0)

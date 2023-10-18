import random, copy

def neighbor(f, p, h):
    for i in range(len(p)):
        p[i] += random.uniform(-h, h)

    return f(p), p

def hillClimbing(f, p, h = 0.01):
    failCount = 0
    while (failCount < 10000):
        fnow = f(p)
        fneighbor, newp = neighbor(f, copy.copy(p), h)
        if fneighbor >= fnow:
            p = newp
            print('p=', p, 'f(p)=', fneighbor)
            failCount = 0
        else:
            failCount = failCount + 1
    return p, fnow

def f(p):
    return -1 * (p[0]**2 + p[1]**2 + p[2]**2)

hillClimbing(f, [2, 1, 3])

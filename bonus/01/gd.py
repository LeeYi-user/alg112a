step = 0.01

# 函數 f 對變數 p[k] 的偏微分: df / dp[k]
def df(f, p, k):
    p1 = p.copy()
    p1[k] = p[k]+step
    return (f(p1) - f(p)) / step

# 梯度：函數 f 在點 p 上的梯度
def grad(f, p):
    gp = p.copy()
    for k in range(len(p)):
        gp[k] = df(f, p, k)
    return gp

def gradientDescent(f, p):
    while True:
        fnow = f(p)
        gp = grad(f, p)
        temp = p.copy()

        for i in range(len(temp)):
            temp[i] -= gp[i] * step

        fneighbor = f(temp)

        if fneighbor < fnow:
            p = temp
            print('p=', p, 'f(p)=', fneighbor)
        else:
            break

def f(p):
    return p[0]**2 + p[1]**2 + p[2]**2

gradientDescent(f, [2, 1, 3])

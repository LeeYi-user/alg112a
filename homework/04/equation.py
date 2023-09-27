from numpy import arange

f0 = lambda x: x**2 - 3*x + 1
f1 = lambda x: (x**2 + 1) / 3
f2 = lambda x: (3*x - 1)**0.5
f3 = lambda x: (3*x - 2) / (x + 1) + 1

for x0 in arange(0, 20, 0.001):
    if abs(f0(x0)) < 0.001:
        print("x0:", x0)

x1, x2, x3 = 1, 1, 1

for i in range(20):
    x1, x2, x3 = f1(x1), f2(x2), f3(x3)
    print("x1:", x1, "x2:", x2, "x3:", x3)

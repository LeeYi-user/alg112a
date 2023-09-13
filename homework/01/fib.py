f = []
n = int(input("請輸入數字: "))

for n in range(n + 1):
    if n == 0:
        f = [0]
    elif n == 1:
        f.append(n)
    else:
        f.append(f[n - 1] + f[n - 2])

print(f"fib({n}) =", f[-1])

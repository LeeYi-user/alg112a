from engine import Value

a = Value(2)
b = Value(1)
c = Value(3)

while True:
    f = a**2 + b**2 + c**2

    print("a=", a.data, "b=", b.data, "c=", c.data, "f=", f.data)
    f.backward()

    if a.grad < 0.001:
        break

    a -= a.grad * 0.01
    b -= b.grad * 0.01
    c -= c.grad * 0.01

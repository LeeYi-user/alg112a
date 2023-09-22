def perm(n):
    p = [0] * n
    print(p)

    while 0 in p:
        for i in range(len(p)):
            if p[i] == 0:
                p[i] = 1
                break
            else:
                p[i] = 0
                i += 1

        print(p[::-1])

perm(4)

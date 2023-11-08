m = [   "********",
        "** * ***",
        "     ***",
        "* ******",
        "*     **",
        "***** **"   ]

n = [[False] * len(m[0]) for i in range(len(m))]

def findPath(x, y):
    if x < 0 or x == len(m) or y < 0 or y == len(m) or m[x][y] == "*" or n[x][y]:
        return True

    n[x][y] = True

    print(x, y)

    if x == len(m) - 1:
        return False

    if findPath(x - 1, y):
        if findPath(x + 1, y):
            if findPath(x, y - 1):
                findPath(x, y + 1)

findPath(2, 0)

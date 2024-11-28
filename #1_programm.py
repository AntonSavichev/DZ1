def tri(a):
    ch = ""
    while a > 0:
        c = a % 3
        a = a // 3
        ch = str(c) + ch
    return ch

for N in range(1, 300):
    c = N
    r = tri(c)
    if N%2 == 0:
        r = "2" + r
    if N%2 == 1:
        r = str(tri(int(r[0:1:]))*2)+r+"2"
    r = int(r, 3)
    if r > 100:
        print(N)



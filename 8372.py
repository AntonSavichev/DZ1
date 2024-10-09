def F(n):
    if n<2:
        return n
    if n>=2:
        return (F(n//2)*10+n%2)

for i in range(1, 2**21):
    if F(i) == 100000100001000100101:
        print(i)
        break
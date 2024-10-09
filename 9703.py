
def F(n):
    if n < 2:
        return n
    if n >= 2:
        return F(n//2) + F(n%2)

coun = 0
for i in range(1, 2**30):
    if F(i) == 27:
        coun += 1
print(coun)

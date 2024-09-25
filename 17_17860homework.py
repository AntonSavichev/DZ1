f = open("17_17680.txt")

def MINPOLO(a):
    b = 0
    for i in range(0, len(a)-1):
        if a[i] > -1 and a[i] < a[i+1] and a[i]%41 == 0:
            b = a[i]
    return b


coun = 0
bol = 0
b = 0

a = f.readlines()
a = [x.rstrip() for x in a]
a = [int(x) for x in a]

c = MINPOLO(a)
print(c)

for i in range(0, len(a)-1,2):
    if (a[i] != a[i+1]) and (((a[i] - a[i+1])* (-1))%c == 0 ):
        coun += 1
    if a[i] + a[i+1] > b:
        b = a[i] + a[i+1]

print(coun)
print(b)


f.close()
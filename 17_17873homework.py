f = open("17_17873.txt")

def MIN(n):
    minim = int(n[1])
    for i in range(0, len(n)-1):
        b = int(n[i])
        if b < minim:
            minim = b
    return minim

coun = 0
bol = 0

a = f.readlines()
a = [line.rstrip() for line in a]

minim = MIN(a)

for i in range(0, len(a)-1):
    b = a[i]
    c = a[i+1]
    if int(b)%16 == minim or int(c)%16 == minim:
        coun += 1
    if int(b)+int(c) > int(bol):
        bol = a[i]+a[i+1]

print(coun)
print(bol)
f.close()
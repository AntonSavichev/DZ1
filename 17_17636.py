f = open("17_17636.txt")

a = f.readlines()
a = [x.rstrip() for x in a]
a = [int(x) for x in a]

def MAX(a):
    maxim = 0
    for i in a:
        b = str(i)
        if i > -1 and b[-1:-2:-1] == "3" and len(b) == 3 and i > maxim:
            maxim = i
    return maxim

coun = 0
Max = 0
maxim = MAX(a)
print(maxim)

for i in range(0, len(a)-2, 3):
    b = str(a[i])
    c = str(a[i+1])
    d = str(a[i+2])
    if ((b[-1:-2:-1] =="3" and len(str(a[i]*(-1))) == 3) or (c[-1:-2:-1] =="3" and len(str(a[i+1]*(-1))) == 3) or (d[-1:-2:-1] =="3" and len(str(a[i+2]*(-1))) == 3)) and (a[i]+a[i+1]+a[i+2] < maxim):
        coun += 1
    if a[i]+a[i+1]+a[i+2] > Max:
        Max = a[i]+a[i+1]+a[i+2]
print(coun)
print(Max)





f.close()
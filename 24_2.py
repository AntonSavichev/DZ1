import fnmatch
import os


f = open("./24-228_5644.txt")

a = f.readline()
p = []
s = 0

a = a.split("XX")

for i in a:
    if i.isdigit() and fnmatch.fnmatch(i, "3????78??45"):
        p.append(i)

p_max = max(p, key=int)

summ = 0
pro = 1
print(p_max)
for i in p_max:
    i = int(i)
    if i%2 == 0:
        summ += i
    elif i%2 != 0:
        pro *= i
print(pro*summ)



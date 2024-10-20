f = open("./24-s1_2555.txt")

a = f.readlines()
k = 0
for i in a:
    y =i.strip()
    if y.count("S") == y.count("X"):
        k+=1
print(k)

f.close()
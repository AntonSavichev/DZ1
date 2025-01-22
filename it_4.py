f = [0]*(10**10)
k = 0

for i in range(0, 10**10):
    if i < 10:
        f[i] = 0
    if i >= 10:
        f[i] = f[i//10]+(i//10%10)-(i%10)
        if f[i] == 9:
            k+=1
print(k)
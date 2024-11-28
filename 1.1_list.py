
С = int(input())

p = [i for i in range(С + 1)]
p[1] = 0
i = 2
while i <= С:
    if p[i] != 0:
        j = i + i
        while j <= С:
            p[j] = 0
            j = j + i
    i += 1
# Избавляемся от всех нулей в списке
p1 = [i for i in p if i != 0]
print(p1)


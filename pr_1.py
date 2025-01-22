import itertools
k = 0

for i in itertools.product("АВНРЬЯ", repeat = 5):
    k+=1
    c = "".join(i)
    if c[0] != "Я" and c.count("Ь") <= 1 and c.count("ЯЯ"):
        print(k)

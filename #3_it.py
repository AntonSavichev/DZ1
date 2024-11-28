import itertools

a = 0
k = 0
for i in itertools.product("АИКМНОПЯ", repeat = 6):
  c = "".join(i)
  k+=1
  if k%2 == 1 and c[0] != "М" and c.count("И") == 3:
    a+=1
print(a)

import itertools

a = 0
for i in itertools.product("012345689ABCDE", repeat = 5):
  c = "".join(i)
  if c.count("8") and (c.count("A") + c.count("B") + c.count("C") + c.count("D") +c.count("E")) > 2:
    a+=1
print(a)
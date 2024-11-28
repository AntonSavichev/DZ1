import fnmatch
import os

for i in range(206, 10**14):
    if i%206 == 0 and fnmatch.fnmatch(str(i), "12?345?67089?"):
        print(i, i//206)

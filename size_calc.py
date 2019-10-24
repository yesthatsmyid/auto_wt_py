#!/bin/python3
import os
totalsize=0

#storing the absolute path of current directory
cwd= os.path.abspath(".")
nwd=os.path.dirname(cwd)
#for every file in current directory:
for filename in os.listdir(nwd):
    totalsize = totalsize + os.path.getsize(os.path.join(nwd, filename
        ))

print("Calculating.............................")
print(totalsize,"KB")

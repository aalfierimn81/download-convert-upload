import os
import sys

#os.chdir(sys.argv[1])

for file in os.listdir():
    if os.path.isfile(file):
        src = file
        dst = str(file).replace(' ','_')
        print("Python---Renaming file...")
        os.rename (src, dst)

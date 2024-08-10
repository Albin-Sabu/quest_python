"""
Write a program to move a file in directory 'source' and copy it to 'destination'. Handle necessary exceptions:
1. if file does not exists in source, print "no file found in source".
2. if same file already exists in target, print "file with same name already exists"

"""

import shutil
import os
print(os.getcwd())
os.mkdir("dir1")
file=open("dir1/file1.txt", 'x')
file.close()
try:
   os.mkdir("dir2") 
except :
    print("File with same name already exists")   

try:
    shutil.copyfile('dir1/file1.txt',"dir2/file2.txt")
except:
    print("No file found in source")
except :
    print("File with same name already exists")
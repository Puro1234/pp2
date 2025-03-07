import os 

path = r"C:\Users\User\Desktop\pp2\lab6\dir-and-files\todelete.txt"

if os.access(path, os.F_OK):
    os.remove(path)
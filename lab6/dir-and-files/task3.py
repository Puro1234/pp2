import os

path = r"C:\Users\User\Documents\bib\NurbakytSerik.pdf"
print("Our path", path)

print("Does our path exists?", os.path.exists(path))

if os.path.exists(path):
    if os.path.isfile(path):
        print("File's name:", os.path.basename(path))
        print("Path to the file:", os.path.dirname(path))
    else: print("Path to the directory:", os.path.dirname(path))
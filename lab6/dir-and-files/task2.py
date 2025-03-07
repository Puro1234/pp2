
import os

path = r'C:\Users\User\Documents\bib'
print("Our path:", path)

print("Does this path exist?", os.access(path, os.F_OK))
print("Can we read it?", os.access(path, os.R_OK))
print("Can we edit it?", os.access(path, os.W_OK))
print("Can we execute it?", os.access(path, os.X_OK))

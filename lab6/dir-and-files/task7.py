import os

file = open("johnny.txt", 'r')
content_to_copy = file.read()

with open("johnny_copy.txt", 'w') as file:
    file.write(content_to_copy)
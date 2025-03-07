import os 

path = r'C:\Users\User\Desktop\pp2\lab6\dir-and-files\alphabet'


for letter in range(65, 91):
    with open((path+'\\'+chr(letter)+'.txt'), 'w') as file:
        pass
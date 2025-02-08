#Define a class which has at least two methods: getString: to get a string from console input printString: to print the string in upper case.

class Strings01:
    def __init__(self):
        self.inputStr = ""
    def getString(self):
        self.inputStr = input()
    def printString(self):
        print(self.inputStr.upper())

test = Strings01()
test.getString() #String01.getString(test)
test.printString()
print(test.inputStr)

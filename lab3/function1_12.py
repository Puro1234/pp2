#Define a functino histogram() that takes a list of integers and prints a histogram to the screen. For example, histogram([4, 9, 7]) should print the following:
#****
#*********
#*******
def histogram(nums):
    for x in nums:
        for i in range(0, int(x)):
            print('*', end = '')
        print()

nums = list(input("Enter numbers separated by spaces: ").split())
histogram(nums)
#Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
#def has_33(nums):
#    pass
#
#has_33([1, 3, 3]) → True
#has_33([1, 3, 1, 3]) → False
#has_33([3, 1, 3]) → False

def has_33(nums):
    for i in range(0, len(nums)-1):
        if int(nums[i]) == 3 and int(nums[i+1]) == 3:
            return True
    return False

nums = list((input("Enter digits separated by spaces: ").split()))
if has_33(nums):
    print("3 is next to 3 indeed")
else:
    print("No, there are no 3s next to each other")
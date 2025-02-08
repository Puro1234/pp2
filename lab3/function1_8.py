#Write a function that takes in a list of integers and returns True if it contains 007 in order
#def spy_game(nums):
#    pass
#
#spy_game([1,2,4,0,0,7,5]) --> True
#spy_game([1,0,2,4,0,5,7]) --> True
#spy_game([1,7,2,0,4,5,0]) --> False

def spy_game(nums):
    for i in range(0, len(nums)-2):
        if int(nums[i]) == 0:
            for j in range(i+1, len(nums)-1):
                if int(nums[j]) == 7:
                    return False
                elif int(nums[j]) == 0:
                    for k in range(j+1, len(nums)):
                        if int(nums[k]) == 0:
                            return False
                        elif int(nums[k]) == 7:
                            return True
    return False

nums = list((input("Enter digits separated by spaces: ").split()))
if spy_game(nums):
    print("If James Bond is the best secret agent in the world, then how does everyone know about him?")
else:
    print("No spies detected")
# This is just an addition to Array3.py where I just see if an array is sorted

def issorted(nums):
    x = sorted(nums)
    if nums == x:
        print("yes")
    else:
        print("no")
def issortedwithextrasteps(nums):
    n = len(nums)
    for i in range(1, n):
        if nums[i] <= nums[i-1]:
            print("no")

    print("yes")

nums = [3,4,5,9,12]
issorted(nums)
issortedwithextrasteps(nums)

        
        
    
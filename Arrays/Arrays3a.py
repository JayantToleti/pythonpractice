#Leetcode-1752
#Check if array is sorted and Rotated
# Given an array nums, return true if the array was originally sorted in non-decreasing order, then rotated some number of positions (including zero). Otherwise, return false.
# There may be duplicates in the original array.

# Approach: 1st check the array in reverse order, if we get an obstacle we stop and search the array in the opposite direction. if we get an obstacle we stop and compare. we check if the array is rotated and return the answer

def l1752(nums):
    for i in range(len(nums)-1, -1, -1):
        if i == 0:
            print("True")
        if nums[i] < nums[i-1]:
            break
    for j in range(i):
        if nums[j]> nums[j+1]:
            break
    if i-j==0 or i-j ==1 and nums[0] >= nums[-1]:
        print("True")
    else:
        print("F")
    

nums = [3,4,5,1,2]
l1752(nums)
#Left rotate array by k places
 
def rotate(nums, k):
    a = [0] * len(nums)
    for i in range(len(nums)):
        a[(i+k)%len(nums)] = nums[i] #recycle

    for i in range(len(nums)):
        nums[i] = a[i]
nums = [1,2,3,4,5,6,7,8]
k = 3
rotate(nums,k)
print(nums)

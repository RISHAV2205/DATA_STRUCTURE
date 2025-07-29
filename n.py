
def rotate(nums, k):
    """
    Do not return anything, modify nums in-place instead.
    """
    k=k%len(nums)
    left,right=0,len(nums)-1
    while left<right:
        nums[left],nums[right]=nums[right],nums[left]
        left+=1
        right-=1

    left,right=0,k-1
    while left<right:
        nums[left],nums[right]=nums[right],nums[left]
        left+=1
        right-=1
    
    left,right=k,len(nums)-1
    while left<right:
        nums[left],nums[right]=nums[right],nums[left]
        left+=1
        right-=1
nums=[-1,-100,3,99]
k=2
rotate(nums,k)
print(nums)
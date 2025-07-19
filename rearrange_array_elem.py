
def rearrangeArray(nums):
    
    pos=0
    neg=1
    res=[0]*len(nums)
    for i in range(len(nums)):
        if pos<len(nums) or neg<len(nums):

            if nums[i]>0:
                res[pos]=nums[i]
                pos+=2
            else:
                res[neg]=nums[i]
                neg+=2
                
    return res
                
nums=[3,-2,1,-5,2,-4]
c=rearrangeArray(nums)
print(c)
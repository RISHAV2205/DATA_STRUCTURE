def searchRange( nums, target):
    li=[-1]*2
    low=0
    high=len(nums)-1
    while low<=high:
        mid=(low+high)//2
        
        if nums[mid]==target:
            first=mid
            last=mid
            
            if mid >0 and nums[mid-1]==target:
                while first>0 and nums[first-1]==target:
                    first-=1
            
            if mid < len(nums)-1 and nums[mid+1]==target:
                while last<len(nums)-1 and nums[last+1] ==target:
                    last+=1
            li[0]=first
            li[1]=last
            return li
        elif nums[mid]>target:
            high=mid-1
        else:
            low=mid+1
    
    return li
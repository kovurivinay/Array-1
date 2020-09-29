def productExceptSelf(self, nums: List[int]) -> List[int]:
    # Time: O(N) + O(N) --> O(N)
    # Space: O(1)

    if not nums:
        return []
    
    res=[1]
    
    for i in range(len(nums)-1):
        res.append(nums[i]*res[-1])
    
    reverse_var=nums[-1]
    for i in range(len(nums)-2,-1,-1):
        res[i]*=reverse_var
        reverse_var*=nums[i]
    
    return res
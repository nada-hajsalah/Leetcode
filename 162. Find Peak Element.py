class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        if len(nums)==1:#case1: [1]
            return 0
        if nums[len(nums)-1]>nums[len(nums)-2]: #case 2: the peek is last item in the list
            return len(nums)-1
        while(l<=r):
            m=(l+r)//2
            if nums[m]>=nums[m-1]:
                if nums[m]>=nums[m+1]:
                    return m
                else:
                    l=m
            else:
                r=m
                

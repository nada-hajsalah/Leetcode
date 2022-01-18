class Solution1:
    #binary search
    def findMin(self, nums: List[int]) -> int:
        r=len(nums)-1
        l=0
        while(l<=r):
            m=(l+r)//2
              if nums[m]>=nums[l] and nums[m]<=nums[r]:# no roated array
                return nums[0]
            if nums[m]<nums[m-1] and nums[m]<nums[m+1]:
                return nums[m]
          
            if nums[m]>=nums[l]:
                if nums[m]<nums[m+1]:
                    l=m+1
                else:
                    return nums[m+1]
            else:
                if nums[m]<nums[m+1]:
                    r=m-1
                else:
                    return nums[m+1]
        return -1

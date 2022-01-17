#Sipmle and easy solution to implement without binary search
class Solution1:
    
    def search(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            return -1
          
#Solution with binary search
class Solution2:
    
    def search(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1
        while left <= right:
            m=(left+right)//2
            if nums[m]==target:
                return m
            #right sorted array
            if nums[m]<=nums[right]:
                if nums[m]>target or nums[right]< target:
                    right=m-1
                else:
                    left=m+1
                
            #left sorted array
            else:
                if nums[m]<target or nums[left]> target:
                    left=m+1
                else:
                    right=m-1
        return -1

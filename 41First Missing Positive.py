class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        a=sorted(nums)
        end=a[-1]
        nex=1
        output=0
     
        for i in range(len(a)):
                if a[i]<=0:
                    output=1
                else:
                    if a[i]==nex:
                        nex=a[i]+1
                        output=0
                    else:
                           output= nex
                            
        if output>0:
            return output
        else:
            return end+1


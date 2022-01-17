import numpy as np
class Solution1:
  # Flatten the matrix into a single array and use BS to find the target
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        matrix_list=list(np.array(matrix).flatten())
        l=0
        r=len(matrix_list)-1
        while(l<=r):
            m=(l+r)//2
            if matrix_list[m]==target:
                return True
            if target>matrix_list[m]:
                l=m+1
            else:
                r=m-1
        return False
      
      
class Solution2:
  #Search the row in which the target could be and use BS in that row
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i=0
        while(i<len(matrix)-1):
            if matrix[i][-1]<target :
                i=i+1
            else:
                break
        matrix_list=matrix[i]
        l=0
        r=len(matrix_list)-1
        while(l<=r):
            m=(l+r)//2
            if matrix_list[m]==target:
                return True
            if target>matrix_list[m]:
                l=m+1
            else:
                r=m-1
        return False
                
                

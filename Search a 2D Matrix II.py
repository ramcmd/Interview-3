# TC: O(m +n) where m is the no of rows and n is the no of columns
# SC: O(1) 

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        p1 = 0
        c = len(matrix[0]) - 1

        while (p1 < (len(matrix)) and c >= 0):
            if matrix[p1][c] == target:
                return True

            elif matrix[p1][c] > target:
                c -= 1

            else:
                p1 += 1
        
        return False
            
            
        
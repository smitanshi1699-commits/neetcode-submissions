class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        rows = len(matrix)
        cols = len(matrix[0])

        left = 0
        right = rows * cols - 1


        while left <= right:

            mid = left + (right - left)//2
            mid_value = matrix [mid // cols][mid % cols]

            if mid_value == target:
                return True
            
            elif mid_value > target:
                right = mid - 1

            else:
                left = mid +1

        return False
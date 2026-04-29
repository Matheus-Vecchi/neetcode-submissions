class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = 0
        j = len(matrix) - 1

        while i <= j:
            mid1 = (j + i) // 2
            
            l = 0
            r = len(matrix[mid1]) - 1

            while l <= r:
                mid2 = (r + l) // 2

                if target > matrix[mid1][mid2]:
                    l = mid2 + 1
                elif target < matrix[mid1][mid2]:
                    r = mid2 - 1
                else:
                    return True
            
            if matrix[mid1][-1] > target:
                j = mid1 - 1
            elif matrix[mid1][-1] < target:
                i = mid1 + 1

        return False
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        
        low = 0
        high = m * n - 1

        while low <= high:
            mid = (low + high) // 2
            row = mid // n
            col = mid % n
            val = matrix[row][col]

            if val > target:
                high = mid - 1

            elif val < target:
                low = mid + 1

            else:
                return True

        return False

        # ✅ Time complexity: O(log(m*n))
        # ✅ Space complexity: O(1)



            

        
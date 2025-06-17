class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # Binary Search Algorithm
        l = 0
        r = num

        while l <= r:
            m = (l + r) // 2
            if m * m > num:
                r = m - 1
            elif m * m < num:
                l = m + 1
            else:
                return True

        return False
        
        # Time Complexity : O(n)
        # Space Complexity : O(1)
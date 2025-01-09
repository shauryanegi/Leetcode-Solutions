class Solution:
    def maxArea(self, height: List[int]) -> int:

        # Brute Force
        # res = 0

        # for l in range(len(height)):
        #     for r in range(l + 1, len(height)):
        #         breadth = (r - l)
        #         length = min(height[l], height[r])
        #         area = breadth * length
        #         res = max(res, area)

        # return res
        
        # Linear Time Solution: O(n), Two Pointers
        res = 0

        l = 0
        r = len(height) - 1

        while l < r:
            breadth = (r - l)
            length = min(height[l], height[r])
            area = breadth * length
            res = max(res, area)

            if height[l] < height[r]:
                l += 1
            elif height[l] > height[r]:
                r -= 1
            else:
                l += 1 # r -= 1 will also work

        return res
            

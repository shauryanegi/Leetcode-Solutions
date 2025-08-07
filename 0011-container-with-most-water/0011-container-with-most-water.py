class Solution:
    def maxArea(self, height: List[int]) -> int:
        # TC: O(n), SC: O(1)
        max_area = 0
        l = 0
        r = len(height) - 1

        while l < r:
            area = min(height[l], height[r]) * (r - l)
            max_area = max(area, max_area)

            if height[l] < height[r]:
                l += 1
            elif height[l] > height[r]:
                r -= 1
            else:
                r -= 1  # or l += 1

        return max_area

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return sum(range(len(nums) + 1)) - sum(nums)

# Time Complexity: O(n) â both sum operations iterate through n elements
# Space Complexity: O(1) â constant extra space is used

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i-1]

        suffix = [1] * len(nums)
        for i in range(len(nums) -2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]

        answer = [1] * len(nums)
        for i in range(len(nums)):
            answer[i] = prefix[i] * suffix[i]

        return answer

# Time Complexity: O(n) — Three passes through the array (prefix, suffix, final answer)
# Space Complexity: O(n) — For prefix, suffix, and answer arrays

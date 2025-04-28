class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(2):
            for num in nums:
                ans.append(num)
        return ans

    # Time complexity: O(n)
    # Space complexity: O(n) for the output array.

        
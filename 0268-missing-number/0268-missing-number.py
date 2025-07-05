class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        # n = len(nums)
        # expected_sum = n * (n + 1) // 2
        # return expected_sum - sum(nums)

        # More Efficient way
        
        xor1 = 0
        xor2 = 0

        for i in range(len(nums)):
            xor1 = xor1 ^ i
            xor2 = xor2 ^ nums[i]

        xor1 = xor1 ^ len(nums) # last element as it got left out in the loop

        return xor1 ^ xor2

        # Time Complexity: O(n), Space Complexity: O(1)

            
        
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxi = cnt = 0

        for num in nums:
            if num == 1:
                cnt += 1
                maxi = max(maxi,cnt)

            else:
                cnt = 0

        return maxi


        # Time Complexity : O(n)
        # Space Complexity: O(1)
        
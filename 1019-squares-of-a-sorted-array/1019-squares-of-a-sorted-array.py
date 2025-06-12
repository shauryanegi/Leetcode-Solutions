class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        # for i in range(len(nums)):
        #     nums[i] == nums[i] ** 2
        #     nums.sort()

        # return nums

        for i in range(len(nums)):
            nums[i] = nums[i] ** 2

        l = 0
        r = len(nums) - 1
        ans = []
        while l <= r:
            if nums[l] >= nums[r]:
                ans.append(nums[l])
                l += 1
            else:
                ans.append(nums[r])
                r -= 1
        ans = ans[::-1]
        return ans

        